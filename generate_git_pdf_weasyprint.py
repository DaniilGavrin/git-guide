#!/usr/bin/env python3
"""
Скрипт генерации PDF из Markdown файла с использованием WeasyPrint.
Воссоздает оригинальный стиль документа с шрифтами Liberation.
"""

import os
import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def create_pdf(input_md, output_pdf):
    # Чтение Markdown файла
    if not os.path.exists(input_md):
        print(f"Ошибка: Файл {input_md} не найден.")
        return
    
    with open(input_md, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Конвертация Markdown в HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['fenced_code', 'codehilite', 'tables']
    )
    
    # Оборачиваем в полный HTML документ
    full_html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Git Commands Full</title>
        <style>
            @font-face {{
                font-family: 'LiberationSans';
                src: url('file:///usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf');
            }}
            @font-face {{
                font-family: 'LiberationSans-Bold';
                src: url('file:///usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf');
            }}
            @font-face {{
                font-family: 'LiberationSans-Italic';
                src: url('file:///usr/share/fonts/truetype/liberation2/LiberationSans-Italic.ttf');
            }}
            @font-face {{
                font-family: 'LiberationMono';
                src: url('file:///usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf');
            }}
            
            body {{
                font-family: 'LiberationSans', sans-serif;
                font-size: 10pt;
                line-height: 1.2;
                color: #000;
                margin: 0;
                padding: 0;
            }}
            
            h1 {{
                font-family: 'LiberationSans-Bold', sans-serif;
                font-size: 12pt;
                text-align: center;
                margin-top: 0pt;
                margin-bottom: 8pt;
                color: #000;
            }}
            
            h2 {{
                font-family: 'LiberationSans-Bold', sans-serif;
                font-size: 11pt;
                text-align: center;
                margin-top: 10pt;
                margin-bottom: 6pt;
                color: #000;
            }}
            
            h3 {{
                font-family: 'LiberationSans-Bold', sans-serif;
                font-size: 10pt;
                text-align: left;
                margin-top: 5pt;
                margin-bottom: 3pt;
                color: #000;
            }}
            
            p {{
                font-family: 'LiberationSans', sans-serif;
                font-size: 10pt;
                margin-top: 2pt;
                margin-bottom: 2pt;
                text-align: left;
            }}
            
            pre {{
                font-family: 'LiberationMono', monospace;
                font-size: 9pt;
                background-color: transparent;
                border: none;
                padding: 0;
                margin-top: 1pt;
                margin-bottom: 2pt;
                overflow-x: auto;
                white-space: pre-wrap;
                word-wrap: break-word;
            }}
            
            code {{
                font-family: 'LiberationMono', monospace;
                font-size: 9pt;
                background-color: transparent;
                padding: 0;
                border-radius: 0;
            }}
            
            pre code {{
                background-color: transparent;
                padding: 0;
                border: none;
            }}
            
            ul, ol {{
                font-family: 'LiberationSans', sans-serif;
                font-size: 10pt;
                margin-top: 2pt;
                margin-bottom: 2pt;
                padding-left: 16pt;
            }}
            
            li {{
                margin-top: 1pt;
                margin-bottom: 1pt;
                list-style-position: outside;
            }}
            
            ol {{
                list-style-type: decimal;
            }}
            
            hr {{
                border: none;
                border-top: 1px solid #ccc;
                margin-top: 8pt;
                margin-bottom: 8pt;
            }}
            
            .footer {{
                font-family: 'LiberationSans-Italic', sans-serif;
                font-size: 9pt;
                text-align: center;
                margin-top: 20pt;
                color: #666;
            }}
            
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 6pt;
                margin-bottom: 6pt;
            }}
            
            th, td {{
                border: 1px solid #ddd;
                padding: 4pt 6pt;
                text-align: left;
                font-size: 9pt;
            }}
            
            th {{
                font-family: 'LiberationSans-Bold', sans-serif;
                background-color: #f5f5f5;
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
    
    # Генерация PDF
    html_doc = HTML(string=full_html)
    css = CSS(string='''
        @page {
            size: A4;
            margin: 1.5cm 1.7cm;
        }
    ''', font_config=font_config)
    
    html_doc.write_pdf(output_pdf, stylesheets=[css], font_config=font_config)
    
    print(f"PDF успешно создан: {output_pdf}")
    
    # Вывод информации о файле
    file_size = os.path.getsize(output_pdf)
    print(f"Размер файла: {file_size / 1024:.1f} KB")

if __name__ == "__main__":
    input_file = "to-print/git-commands-full.md"
    output_file = "to-print/git-commands-full.pdf"
    
    create_pdf(input_file, output_file)
