from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1 — личные данные
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    # Шаг 2 — детали заказа
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    RENT_OPTIONS = {
        "сутки": (By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]'),
        "двое суток": (By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]')
    }

    # Цвет самоката
    COLOR_BLACK = (By.ID, 'black')
    COLOR_GREY = (By.ID, 'grey')

    # Комментарий
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')

    # Кнопка "Заказать"
    ORDER_SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Заказать")]')

    # Модальное окно подтверждения
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')

    # Модальное окно об успешном заказе
    SUCCESS_MODAL = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
