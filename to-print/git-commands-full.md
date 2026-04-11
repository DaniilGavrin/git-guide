# Полная памятка по командам Git

## 1. Настройка и конфигурация

### Глобальная настройка пользователя
```bash
git config --global user.name "Имя Фамилия"
git config --global user.email "email@example.com"
```

### Просмотр конфигурации
```bash
git config --list
git config user.name
git config user.email
```

### Настройка редактора
```bash
git config --global core.editor "nano"
git config --global core.editor "vim"
git config --global core.editor "code --wait"
```

### Настройка цветов
```bash
git config --global color.ui auto
```

---

## 2. Создание и инициализация репозитория

### Инициализация нового репозитория
```bash
git init
git init -b main
```

### Клонирование существующего репозитория
```bash
git clone <url>
git clone <url> <directory-name>
git clone --depth 1 <url>  # Клонирование без истории
git clone --branch <branch-name> <url>
```

---

## 3. Базовая работа с файлами

### Проверка статуса
```bash
git status
git status -s  # Краткий формат
```

### Добавление файлов в индекс (staging area)
```bash
git add <file>
git add .              # Добавить все файлы
git add *.py           # Добавить файлы по маске
git add -p             # Интерактивное добавление частями
git add -A             # Добавить все изменения (включая удаленные)
```

### Удаление файлов из индекса
```bash
git reset HEAD <file>
git rm --cached <file>
```

### Удаление файлов из рабочей директории и индекса
```bash
git rm <file>
git rm -r <directory>
git rm -f <file>       # Принудительное удаление
```

### Перемещение/переименование файлов
```bash
git mv <old-name> <new-name>
```

---

## 4. Коммиты

### Создание коммита
```bash
git commit -m "Сообщение коммита"
git commit -am "Сообщение"  # Add + Commit для измененных файлов
git commit --amend          # Изменить последний коммит
git commit --amend -m "Новое сообщение"
git commit --no-edit        # Amend без изменения сообщения
```

### Просмотр истории коммитов
```bash
git log
git log --oneline
git log --graph
git log --graph --oneline --all
git log -n 5                # Последние 5 коммитов
git log --since="2 weeks ago"
git log --until="2023-01-01"
git log --author="Имя"
git log --stat              # Статистика изменений
git log -p                  # С полными диффами
```

---

## 5. Ветки (Branches)

### Работа с ветками
```bash
git branch                  # Список локальных веток
git branch -a               # Все ветки (локальные + удаленные)
git branch -r               # Только удаленные ветки
git branch <name>           # Создать ветку
git branch -d <name>        # Удалить ветку (безопасно)
git branch -D <name>        # Удалить ветку (принудительно)
git branch -m <old> <new>   # Переименовать ветку
git branch -v               # Подробный список с последними коммитами
```

### Переключение между ветками
```bash
git checkout <branch-name>
git checkout -b <new-branch>  # Создать и переключиться
git switch <branch-name>      # Современная альтернатива checkout
git switch -c <new-branch>
```

### Слияние веток (Merge)
```bash
git merge <branch-name>
git merge --no-ff <branch>    # Слияние без fast-forward
git merge --squash <branch>   # Слияние в один коммит
git merge --abort             # Отменить слияние при конфликте
```

### Rebase (перебазирование)
```bash
git rebase <branch-name>
git rebase -i HEAD~3          # Интерактивный rebase последних 3 коммитов
git rebase --continue
git rebase --abort
git rebase --skip
```

---

## 6. Удаленные репозитории (Remote)

### Управление удаленными репозиториями
```bash
git remote -v                 # Показать удаленные репозитории
git remote add <name> <url>   # Добавить удаленный репозиторий
git remote remove <name>      # Удалить удаленный репозиторий
git remote rename <old> <new> # Переименовать
git remote set-url <name> <new-url>
```

### Синхронизация с удаленным репозиторием
```bash
git fetch                     # Получить изменения без слияния
git fetch --all               # Получить все удаленные репозитории
git fetch --prune             # Удалить ссылки на удаленные ветки которых нет
git pull                      # Fetch + Merge
git pull --rebase             # Fetch + Rebase
git push                      # Отправить изменения
git push -u origin <branch>   # Push с установкой upstream
git push --force              # Принудительный push (осторожно!)
git push --force-with-lease   # Безопасный принудительный push
git push --delete origin <branch>  # Удалить ветку на сервере
```

---

## 7. Откат изменений

### Отмена изменений в рабочей директории
```bash
git restore <file>            # Восстановить файл до состояния в индексе
git restore --staged <file>   # Убрать файл из индекса
git restore --source=<commit> <file>
git checkout -- <file>        # Старый синтаксис
```

### Отмена коммитов
```bash
git revert <commit-hash>      # Создать новый коммит, отменяющий указанный
git revert HEAD~2..HEAD       # Отменить несколько коммитов
```

### Сброс к предыдущему состоянию
```bash
git reset --soft HEAD~1       # Отменить коммит, оставить изменения в индексе
git reset --mixed HEAD~1      # Отменить коммит, оставить изменения в рабочей директории
git reset --hard HEAD~1       # Полностью отменить коммит и изменения
git reset --hard <commit-hash>
```

### Stash (временное сохранение)
```bash
git stash                     # Сохранить изменения
git stash save "message"      # Сохранить с сообщением
git stash list                # Список всех stash
git stash pop                 # Применить и удалить последний stash
git stash apply               # Применить без удаления
git stash drop                # Удалить stash
git stash clear               # Очистить все stash
git stash show                # Показать изменения в stash
git stash branch <name>       # Создать ветку из stash
```

### Reflog (журнал действий)
```bash
git reflog                    # История всех действий
git reflog show <branch>
git reset --hard HEAD@{2}     # Вернуться к состоянию из reflog
```

---

## 8. Теги (Tags)

### Работа с тегами
```bash
git tag                       # Список всех тегов
git tag -l "v1.*"             # Поиск тегов по шаблону
git tag v1.0.0                # Создать легковесный тег
git tag -a v1.0.0 -m "Message" # Создать аннотированный тег
git tag -d v1.0.0             # Удалить тег локально
git push origin v1.0.0        # Отправить тег на сервер
git push origin --tags        # Отправить все теги
git push --delete origin v1.0.0
```

---

## 9. Поиск и анализ

### Поиск в истории
```bash
git log --grep="текст"
git log -S "функция"          # Найти коммиты где изменилось количество вхождений
git log -G "regex"            # Поиск по регулярному выражению
```

### Поиск в коде
```bash
git grep "текст"
git grep -n "текст"           # С номерами строк
git grep -c "текст"           # Количество вхождений
git grep --cached "текст"     # Поиск в индексе
```

### Анализ изменений
```bash
git diff                      # Изменения в рабочей директории
git diff --staged             # Изменения в индексе
git diff <commit1> <commit2>
git diff <branch1>..<branch2>
git diff --stat               # Статистика изменений
git diff --name-only          # Только имена файлов
git blame <file>              # Кто и когда изменил каждую строку
git blame -L 10,20 <file>     # Blame для конкретных строк
```

### Статистика
```bash
git shortlog -sn              # Количество коммитов по авторам
git shortlog -sn --all
git count-objects -v          # Статистика объектов
git gc                        # Оптимизация репозитория
```

---

## 10. Cherry-pick

### Применение отдельных коммитов
```bash
git cherry-pick <commit-hash>
git cherry-pick <commit1> <commit2>
git cherry-pick <start>^..<end>  # Диапазон коммитов
git cherry-pick --abort
git cherry-pick --continue
git cherry-pick --no-commit
```

---

## 11. Подмодули (Submodules)

### Работа с подмодулями
```bash
git submodule add <url> <path>
git submodule init
git submodule update
git submodule update --recursive
git submodule status
git submodule foreach <command>
git submodule deinit <path>
git rm <submodule-path>
```

---

## 12. Хуки (Hooks)

### Управление хуками
Хуки находятся в `.git/hooks/`
```bash
# Примеры хуков:
# pre-commit - перед коммитом
# post-commit - после коммита
# pre-push - перед отправкой
# prepare-commit-msg - перед редактированием сообщения коммита
```

---

## 13. Конфликты слияния

### Разрешение конфликтов
```bash
# При возникновении конфликта:
# 1. Открыть файлы с конфликтами
# 2. Выбрать нужную версию кода
# 3. git add <resolved-file>
# 4. git commit (или git rebase --continue)

git mergetool               # Запустить инструмент слияния
git diff --conflict-diff-algorithm=histogram
```

---

## 14. Продвинутые операции

### Переписывание истории
```bash
git filter-branch           # Устаревший способ
git filter-repo             # Современный способ (требует установки)
# Удалить файл из всей истории:
git filter-repo --path <file> --invert-paths
```

### Архивирование
```bash
git archive -o latest.zip HEAD
git archive -o latest.tar.gz --prefix=project/ v1.0.0
```

### Worktree (несколько рабочих деревьев)
```bash
git worktree add <path> <branch>
git worktree list
git worktree remove <path>
git worktree prune
```

### Bisect (поиск бага)
```bash
git bisect start
git bisect good <commit>
git bisect bad <commit>
git bisect run <test-script>
git bisect reset
```

---

## 15. Стратегии ветвления

### Git Flow
- `main` / `master` — продакшн
- `develop` — разработка
- `feature/*` — новые функции
- `release/*` — подготовка релиза
- `hotfix/*` — срочные исправления

### GitHub Flow
- `main` — основная ветка
- `feature/*` — ветки для задач
- Pull Request → Review → Merge

### GitLab Flow
- `main` — основная ветка
- Ветки для функций
- Environment branches (pre-production, production)

---

## 16. Безопасность

### Подписанные коммиты
```bash
git config --global user.signingkey <key-id>
git config --global commit.gpgsign true
git commit -S -m "Подписанный коммит"
git log --show-signature
```

### Проверка целостности
```bash
git fsck                   # Проверка целостности базы данных
git verify-pack <pack-file>
```

---

## 17. Решение проблем

### Очистка
```bash
git clean -n               # Показать что будет удалено
git clean -f               # Удалить неотслеживаемые файлы
git clean -fd              # Удалить файлы и директории
git clean -fx              # Удалить включая игнорируемые
```

### Восстановление после ошибок
```bash
# Случайный commit не в ту ветку:
git reset --hard HEAD~1
git checkout <correct-branch>
git cherry-pick <commit-hash>

# Случайное удаление ветки:
git reflog
git branch <name> <commit-hash>
```

### Оптимизация
```bash
git gc --aggressive
git prune
git repack -a -d --depth=250 --window=250
```

---

## 18. Алиасы (Aliases)

### Создание алиасов
```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "reset HEAD --"
git config --global alias.lg "log --oneline --graph --all"
```

### Примеры использования
```bash
git st      # вместо git status
git co -b   # вместо git checkout -b
git lg      # красивый лог
```

---

## 19. Интеграция с CI/CD

### Типичные команды в пайплайнах
```bash
git clone --depth 1 --branch <branch> <url>
git fetch --unshallow         # Для полной истории
git checkout <commit-hash>
```

---

## 20. Полезные советы

1. Всегда делайте `git pull --rebase` вместо обычного `pull`
2. Используйте интерактивный rebase для очистки истории перед merge
3. Пишите понятные сообщения коммитов
4. Делайте маленькие коммиты с одной логической задачей
5. Используйте `.gitignore` для исключения лишних файлов
6. Регулярно делайте `git fetch --prune`
7. Проверяйте `git status` перед коммитом
8. Используйте `git diff --staged` перед коммитом

---

*Документ создан для печати как полная памятка по Git*
