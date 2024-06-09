# Проект автоматизации тестирования с использованием Selenium и Pytest
В проекте реализованы автоматизированные тесты для трех сценариев из ТЗ и для двух сценариев дополнительно.

Используется Selenium WebDriver и фреймворк pytest c плагином pytest_check.

В качестве проверяемого объекта используется сайт: https://mega.readyscript.ru/

Запуск тестов возможен в двух режимах:
* На локальной машине
* С использованием docker контейнера

## Сценарии из ТЗ
### 1. Зарегистрировать пользователя руками и на основании данных реализовать тест на проверку логина на сайт
Тесты: 
* tests/test_authorization.py::TestSuiteAuthorization::test_user_authorization.py
### 2. Проверить переход и отображение товаров в каталоге(синяя кнопка сверху) Электроника -> Планшеты -> Digma
Тесты: 
* tests/test_products.py::TestSuiteProduct::test_open_catalog_page_from_catalog_menu.py
* test_product_in_catalog_page.py
### 3. Проверить добавление товара в корзину и удаление из корзины
* tests/test_products.py::TestSuiteProduct::test_add_delete_products_to_cart.py

## Дополнительные сценарии
### 1. Проверить отсутствие возможности авторизации пользователя с невалидными данными
Тесты: 
* tests/test_authorization.py::TestSuiteAuthorization::TestSuiteAuthorizationNegative::test_user_authorization_negative.py
### 2. Проверить нахождение товара по поисковым запросам в строке поиска
Тесты: 
* tests/test_products.py::TestSuiteProduct::test_search_product_for_query_in_search_bar.py

## Использование
### Запуск на локальной машине с установленным Chrome и Python 3
1. Создайте виртуальное окружение и установите зависимости из `requirements.txt`
2. Запустите тесты
```shell
  pytest -sv
```
### Запуск тестов в контейнере
1. Создайте контейнер с тестами
```shell
  docker build -t tests .
```
2. Запустите контейнер с тестами
```shell
  docker run --rm  tests 
```