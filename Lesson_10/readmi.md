# Проект автотестов с Page Object и Allure

## Установка и запуск

```bash
# Установка зависимостей
pip install selenium pytest allure-pytest

# Запуск всех тестов
pytest --alluredir=allure-results

# Запуск тестов формы
pytest test_01_form_page_obj.py --alluredir=allure-results

# Запуск тестов калькулятора
pytest test_02_calc_page_obj.py --alluredir=allure-results

# Запуск тестов магазина
pytest test_03_shop_page_obj.py --alluredir=allure-results

# Просмотр отчета в браузере
allure serve allure-results

# Или генерация статического отчета
allure generate allure-results -o allure-report --clean

# Затем открыть allure-report/index.html
```

## Структура проекта

```
lesson_10/
├── CalcMainPage.py              # Page Object для калькулятора
├── FormPage.py                  # Page Object для формы
├── ShopPage.py                  # Page Object для магазина
├── test_01_form_page_obj.py     # Тесты формы отправки данных
├── test_02_calc_page_obj.py     # Тесты калькулятора с задержками
├── test_03_shop_page_obj.py     # Тесты интернет-магазина
├── requirements.txt             # Файл зависимостей
├── README.md                    # Этот файл
└── .gitignore                   # Файл для игнорирования (рекомендуется добавить)
```

## Описание тестов

### 1. Тест формы (test_01_form_page_obj.py)
- **Цель:** Проверить валидацию формы
- **Шаги:** Открытие → Заполнение → Отправка → Проверка
- **Ожидание:** Поле zip-code показывает ошибку, остальные поля — успех

### 2. Тест калькулятора (test_02_calc_page_obj.py)
- **Цель:** Проверить математические операции
- **Операции:** Сложение, вычитание, умножение, деление
- **Особенность:** Учет задержки вычислений (5-20 секунд)

### 3. Тест магазина (test_03_shop_page_obj.py)
- **Цель:** Проверить оформление заказа
- **Процесс:** Авторизация → Добавление товаров → Оформление
- **Ожидание:** Итоговая сумма = $58.29