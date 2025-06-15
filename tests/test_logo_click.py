import pytest
import allure
from pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature('Навигация по логотипам')
class TestLogoNavigation:

    @allure.title('Клик по логотипу "Самокат" возвращает на главную страницу')
    @allure.description('Проверяем, что при переходе на страницу заказа и клике по логотипу "Самокат" происходит возврат на главную.')
    def test_click_scooter_logo_redirects_to_main(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open()
        with allure.step("Переходим на страницу заказа и кликаем по логотипу Самокат"):
            page.click_order_button_top()
            page.click_logo_scooter()
        with allure.step("Проверяем, что URL содержит 'qa-scooter'"):
            assert "qa-scooter" in page.get_current_url()

    @allure.title('Клик по логотипу "Яндекс" открывает Дзен в новой вкладке')
    @allure.description('Проверяем, что клик по логотипу Яндекса открывает новую вкладку с сайтом dzen.ru.')
    def test_click_yandex_logo_opens_dzen(self, driver):
        page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            page.open()
        with allure.step("Кликаем по логотипу Яндекса и переключаемся на новую вкладку"):
            page.click_logo_yandex()
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
            page.switch_to_new_tab()
            WebDriverWait(driver, 10).until(lambda d: d.current_url != "about:blank")
        with allure.step("Проверяем, что новая вкладка содержит 'dzen.ru' в URL"):
            assert "dzen.ru" in page.get_current_url()
