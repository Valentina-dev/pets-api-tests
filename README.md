## API-тесты приложения Petstore

**Перед запуском тестов установить зависимости проекта используя команду:**
- `pip install -r requirements.txt`

**Запуск всех тестов производится командой:**
- `pytest -s -v --alluredir=./allure-results`

**Запуск smoke тестов:**
- `pytest -s -v -m smoke main.py `

**Получение allure-отчета:**
- `allure serve allure-results`  

**Запуск тестов через докер:**
- ` docker run -d test-pytest pytest -s -v main.py`

[API Docs](https://petstore.swagger.io/)




