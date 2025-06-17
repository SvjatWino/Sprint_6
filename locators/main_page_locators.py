from selenium.webdriver.common.by import By


class MainPageLocators:
    # Верхняя кнопка "Заказать"
    ORDER_BUTTON_TOP = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]')

    # Нижняя кнопка "Заказать"
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')

    # Логотип "Самокат"
    SCOOTER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')

    # Логотип Яндекс
    YANDEX_LOGO = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')

    # Блок "Вопросы о важном"
    # Вопросы
    FAQ_QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7"),
    ]

    # Ответы
    FAQ_ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7"),
    ]

    # Для принятия куков
    COOKIE_ACCEPT_BUTTON = (By.ID, 'rcc-confirm-button')
