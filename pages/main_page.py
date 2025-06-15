from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    def click_logo_yandex(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    def click_question(self, question_locator):
        self.click(question_locator)

    def get_answer_text(self, answer_locator):
        return self.get_element_text(answer_locator)
