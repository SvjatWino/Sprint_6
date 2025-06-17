import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData


@pytest.mark.parametrize('user', TestData.USERS)
@pytest.mark.parametrize('order_button', ['top', 'bottom'])
@allure.feature('Форма заказа самоката')
class TestScooterOrder:

    @allure.title('Проверка заказа самоката через кнопку "{order_button}"')
    @allure.description('Заполняем форму заказа самоката данными пользователя и проверяем, что заказ оформлен успешно.')
    def test_order_scooter_flow(self, driver, user, order_button):
        with allure.step("Открываем главную страницу"):
            main_page = MainPage(driver)
            main_page.open()

        with allure.step(f"Нажимаем кнопку заказа в {order_button} части страницы"):
            if order_button == 'top':
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        with allure.step("Переходим на страницу заказа"):
            order_page = OrderPage(driver)

        with allure.step("Заполняем личные данные"):
            order_page.fill_personal_info(
                first_name=user['first_name'],
                last_name=user['last_name'],
                address=user['address'],
                metro=user['metro'],
                phone=user['phone']
            )

        with allure.step("Заполняем данные аренды"):
            order_page.fill_date(user['date'])
            order_page.select_rental_period(user['rental_period'])
            order_page.select_color(user['color'])
            order_page.fill_comment(user['comment'])
            order_page.click_order_button_in_form()

        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()

        with allure.step("Проверяем, что заказ оформлен успешно"):
            success_message = order_page.get_success_message()
            assert success_message is not None and success_message != "", "Ожидалось успешное сообщение о заказе"
