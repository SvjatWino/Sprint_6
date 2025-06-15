# Sprint_6

## Описание
Проект представляет собой автоматизированные UI-тесты для веб-сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/), 
выполненные с использованием **Selenium WebDriver**, **pytest**, **Page Object Model** и **Allure** для генерации отчётов.

## Структура проекта

```
Sprint_6/
│
├── data.py                 # Тестовые данные
├── requirements.txt        # Зависимости
├── .gitignore              # Исключения для Git
├── README.md               # Документация проекта
│
├── locators/               # Локаторы элементов
│   ├── __init__.py
│   ├── main_page_locators.py
│   └── order_page_locators.py
│
├── pages/                  # Page Object-классы
│   ├── __init__.py
│   ├── base_page.py
│   ├── main_page.py
│   └── order_page.py
│
├── tests/                  # Тесты по функциональности
│   ├── __init__.py
│   ├── test_main_page.py
│   ├── test_logo_click.py
│   └── test_order_page.py
│
├── allure-results/         # Результаты тестов для Allure (добавлены в репозиторий)

```

## Запуск тестов

Для запуска всех тестов:
```bash
pytest --alluredir=allure-results
```
