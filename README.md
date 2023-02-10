# Тестовое задание для компании "HFLabs"

## Задание
В [базе знаний](https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999) есть информация о кодах ответа нашего API.
Необходимо написать скрипт, который парсит эту табличку и переносит ее в гуглодоку. Предусмотреть, что в будущем необходимо будет синхронизировать данные в гуглодоке, если что-то изменится в базе знаний.

## Установка
1. Склонировать репозиторий
2. Установить зависимости
* для Linux
    ```bash
    pip -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
* для Windows
    ```bash
    python -m venv venv
    venv\Scripts\activate.bat
    pip install -r requirements.txt
    ```
3. В корне проекта поместить файл `credentials.json` с [сервисным аккаунтом](https://cloud.google.com/docs/authentication/getting-started#creating_the_service_account) для доступа к гуглодоке

## Запуск
```bash
python main.py
```
