# Настройка удаленных репозиториев

Удаленные репозитории позволяют синхронизировать вашу работу с командой и хранить код на серверах (GitHub, GitLab, Bitbucket).

## Что такое remote?

Remote (удаленный репозиторий) — это версия вашего проекта, размещенная в сети. У вас может быть несколько удаленных репозиториев, каждый со своим именем.

## Просмотр удаленных репозиториев

```bash
# Показать список remote-ов
git remote

# Подробная информация (URL для чтения и записи)
git remote -v
```

Обычно по умолчанию существует remote с именем `origin` — это тот репозиторий, из которого вы сделали клон.

## Добавление удаленного репозитория

Если вы создали локальный репозиторий и хотите связать его с GitHub:

```bash
git remote add origin https://github.com/username/repo.git
```

Или через SSH (рекомендуется для постоянной работы):
```bash
git remote add origin git@github.com:username/repo.git
```

Проверьте добавление:
```bash
git remote -v
```

## Изменение URL удаленного репозитория

Если URL изменился или вы хотите переключиться с HTTPS на SSH:

```bash
git remote set-url origin git@github.com:username/repo.git
```

## Удаление удаленного репозитория

```bash
git remote remove origin
# или
git remote rm origin
```

## Переименование remote

```bash
git remote rename origin upstream
```
(Часто используется, когда вы делаете fork чужого репозитория: `origin` — ваш форк, `upstream` — оригинал).

## Получение информации о remote

```bash
# Информация о конкретном remote
git remote show origin
```
Покажет отслеживаемые ветки, статус push/pull и другую полезную информацию.

## Работа с несколькими remote

Вы можете иметь несколько удаленных репозиториев. Например:
- `origin` — ваш личный форк на GitHub.
- `upstream` — оригинальный репозиторий, откуда взяли код.

Синхронизация с upstream:
```bash
git fetch upstream
git merge upstream/main
```

---
[Назад: Rebase →](../branching/rebase.md) | [Далее: Push и Pull →](sync.md)
