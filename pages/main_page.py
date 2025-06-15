import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Нажимаем на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.accept_cookies_if_present()
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажимаем на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.accept_cookies_if_present()
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликаем по логотипу Самоката")
    def click_logo_scooter(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликаем по логотипу Яндекса")
    def click_logo_yandex(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Кликаем по вопросу в FAQ")
    def click_question(self, question_locator):
        self.click(question_locator)

    @allure.step("Получаем текст ответа на вопрос в FAQ")
    def get_answer_text(self, answer_locator):
        return self.get_element_text(answer_locator)
