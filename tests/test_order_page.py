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
            order_page.fill_order_info(
                date=user['date'],
                comment=user['comment'],
                color=user['color']
            )

        with allure.step("Подтверждаем заказ"):
            order_page.submit_order()

        with allure.step("Проверяем, что заказ оформлен успешно"):
            assert order_page.order_successful()
