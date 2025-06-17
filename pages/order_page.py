import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполняем личные данные: {first_name} {last_name}, адрес: {address}, метро: {metro}, телефон: {phone}")
    def fill_personal_info(self, first_name, last_name, address, metro, phone):
        self.input_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.input_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.input_text(OrderPageLocators.METRO_INPUT, metro)
        self.select_from_dropdown_by_text(metro)
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click_next()

    @allure.step("Нажимаем кнопку 'Далее'")
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем дату аренды: {date}")
    def fill_date(self, date):
        self.input_text_and_escape(OrderPageLocators.DATE_INPUT, date)

    @allure.step("Выбираем срок аренды: {rental_period}")
    def select_rental_period(self, rental_period):
        self.click(OrderPageLocators.RENT_DROPDOWN)
        self.click(OrderPageLocators.RENT_OPTIONS[rental_period])

    @allure.step("Выбираем цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)

    @allure.step("Вводим комментарий: {comment}")
    def fill_comment(self, comment):
        self.input_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Нажимаем кнопку 'Заказать' в форме")
    def click_order_button_in_form(self):
        self.click(OrderPageLocators.ORDER_BUTTON_IN_FORM)

    @allure.step("Подтверждаем заказ")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получаем текст из модального окна успешного заказа")
    def get_success_message(self):
        return self.get_element_text(OrderPageLocators.SUCCESS_MODAL)
