#!/usr/bin/env python3
"""
Генератор PDF из Markdown для Git шпаргалки.
Использует WeasyPrint и шрифты Liberation для точного воспроизведения оригинала v1.0.0.

Параметры воссозданы по анализу оригинального PDF:
- Шрифты: Liberation-Sans-Bold, Liberation-Mono, Liberation-Sans-Italic
- Размеры: 16pt (главный заголовок), 12pt (H1), 11pt (H2/H3), 9pt (код), 10pt (текст/italic)
- Отступы точно как в оригинале
"""

import os
import re
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


def convert_md_to_html(md_path):
    """Конвертирует Markdown в HTML с правильной разметкой как в оригинале."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    html_lines = []
    lines = content.split('\n')
    in_code_block = False
    code_buffer = []
    
    for line in lines:
        # Обработка блоков кода
        if line.startswith('```'):
            if in_code_block:
                # Закрываем блок кода - каждая строка отдельно
                for code_line in code_buffer:
                    if code_line.strip():
                        html_lines.append(f'<div class="code-line">{code_line}</div>')
                    else:
                        html_lines.append('<div class="code-line">&nbsp;</div>')
                html_lines.append('</div>')
                code_buffer = []
                in_code_block = False
            else:
                html_lines.append('<div class="code-block">')
                in_code_block = True
            continue
        
        if in_code_block:
            # Экранирование HTML внутри кода
            code_line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            code_buffer.append(code_line)
            continue
            
        # Пропуск пустых строк (они обрабатываются через отступы в CSS)
        if not line.strip():
            continue

        # Заголовки
        if line.startswith('# '):
            html_lines.append(f'<h1 class="main-title">{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2 class="section-title">{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3 class="subsection-title">{line[4:]}</h3>')
        # Разделители
        elif line.startswith('---'):
            html_lines.append('<hr class="section-divider"/>')
        # Курсив в конце (финальная строка)
        elif line.startswith('*') and line.endswith('*'):
            text = line[1:-1]
            html_lines.append(f'<p class="footer-note">{text}</p>')
        else:
            # Обычный текст (подзаголовки описаний)
            text = line
            # Обработка inline кода (если есть)
            text = re.sub(r'`([^`]+)`', r'<code class="inline">\1</code>', text)
            # Обработка жирного
            text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
            html_lines.append(f'<p class="description">{text}</p>')

    return '\n'.join(html_lines)


def generate_pdf(input_md, output_pdf):
    """Генерирует PDF файл из Markdown с точными параметрами оригинала."""
    
    # Конвертация в HTML
    html_content = convert_md_to_html(input_md)
    
    # Полный HTML документ
    full_html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Полная памятка по командам Git</title>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
                @bottom-right {{
                    content: counter(page);
                    font-family: "Liberation Sans", sans-serif;
                    font-size: 9pt;
                    color: #666;
                    padding-top: 10pt;
                }}
            }}
            
            body {{
                font-family: "Liberation Sans", sans-serif;
                font-size: 10pt;
                line-height: 1.3;
                color: #000;
                orphans: 2;
                widows: 2;
            }}
            
            /* Главный заголовок */
            h1.main-title {{
                font-family: "Liberation Sans Bold", sans-serif;
                font-size: 16pt;
                text-align: center;
                margin-top: 0pt;
                margin-bottom: 26pt;
                page-break-after: avoid;
            }}
            
            /* Заголовки разделов (##) */
            h2.section-title {{
                font-family: "Liberation Sans Bold", sans-serif;
                font-size: 12pt;
                text-align: center;
                margin-top: 30pt;
                margin-bottom: 18pt;
                page-break-after: avoid;
            }}
            
            /* Подзаголовки (### и описания) */
            h3.subsection-title,
            p.description {{
                font-family: "Liberation Sans Bold", sans-serif;
                font-size: 11pt;
                text-align: left;
                margin-top: 14pt;
                margin-bottom: 10pt;
                page-break-after: avoid;
            }}
            
            /* Блок кода */
            div.code-block {{
                margin-top: 8pt;
                margin-bottom: 14pt;
                padding-left: 8pt;
                page-break-inside: avoid;
            }}
            
            /* Строка кода */
            div.code-line {{
                font-family: "Liberation Mono", monospace;
                font-size: 9pt;
                line-height: 1.4;
                margin: 0;
                padding: 0;
                white-space: pre;
            }}
            
            /* Inline код */
            code.inline {{
                font-family: "Liberation Mono", monospace;
                font-size: 9pt;
                background-color: transparent;
                padding: 0;
            }}
            
            /* Разделитель */
            hr.section-divider {{
                border: none;
                border-top: 1px solid #ccc;
                margin: 20pt 0;
            }}
            
            /* Финальная заметка */
            p.footer-note {{
                font-family: "Liberation Sans Italic", sans-serif;
                font-size: 10pt;
                font-style: italic;
                text-align: left;
                margin-top: 20pt;
                margin-bottom: 0;
            }}
            
            strong {{
                font-family: "Liberation Sans Bold", sans-serif;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Настройка шрифтов
    font_config = FontConfiguration()
    
    css = CSS(string="""
        @font-face {
            font-family: "Liberation Sans";
            src: url("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf");
        }
        @font-face {
            font-family: "Liberation Sans Bold";
            src: url("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf");
        }
        @font-face {
            font-family: "Liberation Sans Italic";
            src: url("/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf");
        }
        @font-face {
            font-family: "Liberation Mono";
            src: url("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf");
        }
    """, font_config=font_config)
    
    # Генерация PDF
    html_doc = HTML(string=full_html)
    html_doc.write_pdf(output_pdf, stylesheets=[css], font_config=font_config)
    
    print(f"✅ PDF успешно создан: {output_pdf}")
    
    # Вывод статистики
    try:
        import subprocess
        result = subprocess.run(['pdfinfo', output_pdf], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'Pages' in line or 'File size' in line:
                print(f"   {line}")
    except Exception:
        pass


if __name__ == "__main__":
    input_file = "to-print/git-commands-full.md"
    output_file = "to-print/git-commands-full.pdf"
    
    if not os.path.exists(input_file):
        print(f"❌ Ошибка: Файл {input_file} не найден!")
        exit(1)
    
    generate_pdf(input_file, output_file)
