# Бот для сбора баллов ЕГЭ через Telegram

Данный бот умеет:
* Регистрировать новых пользователей
* Сохранять их данные в БД
* Сохранять данные о результатах ЕГЭ
* Просматривать свои результаты

## Стек
* `python 3.12`
* `aiogram`
* `SQLAlchemy`
* `Postgresql`


### Работа с зависимостями
* Устанавливаем `pip-compile`
```bash
pip install pip-tools
```
* Добавляем новую зависимость в список `project.dependencies` в `pyproject.toml`
* Генерируем обновленный `requirements.txt`
```bash
pip-compile -o requirements.txt pyproject.toml
```
* Устанавливаем зависимости
```bash
pip install -r requirements.txt
```
#### Добавление `dev` зависимости проекта:
* Добавляем новую зависимость в список `dev` в `project.optional-dependencies` в `pyproject.toml`
* Генерируем обновленный `requirements-dev.txt`
```bash
pip-compile --extra=dev -o requirements-dev.txt pyproject.toml
```
* Устанавливаем `dev` зависимости
```bash
pip install -r requirements-dev.txt
```

## Конфигурация:
* Переменные окружения берутся из файла `.environment`

## Запуск:
* Локально: `python main.py`

## Линтеры:

### pre-commit

1. Запустить скрипт:

   ```shell
   pre-commit run -a
   ```
