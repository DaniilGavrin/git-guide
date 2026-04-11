# Установка и настройка Git

Первый шаг в работе с Git — правильная установка и базовая настройка.

## Установка

### Windows
1. Скачайте установщик с [официального сайта](https://git-scm.com/download/win).
2. Запустите установку, оставляя настройки по умолчанию (рекомендуется).
3. После установки перезапустите терминал или Git Bash.

### macOS
```bash
# Через Homebrew (рекомендуется)
brew install git

# Или через Xcode Command Line Tools
xcode-select --install
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git
```

### Linux (CentOS/RHEL/Fedora)
```bash
sudo dnf install git
# или для старых версий
sudo yum install git
```

## Базовая настройка

После установки необходимо представиться системе. Эти данные будут прикрепляться к каждому вашему коммиту.

```bash
# Установка имени пользователя
git config --global user.name "Ваше Имя"

# Установка email
git config --global user.email "your.email@example.com"
```

> **Важно:** Используйте тот же email, что и в аккаунте GitHub/GitLab, чтобы ваши коммиты корректно связывались с профилем.

### Проверка настроек
```bash
git config --list
```

### Настройка редактора по умолчанию
Git использует системный редактор (часто Vim), но вы можете изменить его:

```bash
# Для VS Code
git config --global core.editor "code --wait"

# Для Nano
git config --global core.editor nano

# Для Sublime Text
git config --global core.editor "subl -n -w"
```

### Настройка цвета вывода
```bash
git config --global color.ui true
```

### Настройка ветки по умолчанию
Современный стандарт — использовать `main` вместо `master`:
```bash
git config --global init.defaultBranch main
```

## Проверка версии
Убедитесь, что Git установлен корректно:
```bash
git --version
```

## Глобальные алиасы (сокращения)
Для ускорения работы можно создать короткие команды:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.last 'log -1 HEAD'
git config --global alias.lg "log --oneline --graph --all"
```
Теперь вместо `git status` можно писать `git st`.

---
[Далее: Начало работы →](init.md)
