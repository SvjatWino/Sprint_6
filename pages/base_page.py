import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru"

    @allure.step("Открываем страницу: {url}")
    def open(self, url=""):
        self.driver.get(self.base_url + url)

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Вводим текст '{text}' в элемент: {locator}")
    def input_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст из элемента: {locator}")
    def get_element_text(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text

    @allure.step("Ожидаем видимость элемента: {locator}")
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step("Принимаем cookies, если появилось окно")
    def accept_cookies_if_present(self):
        try:
            self.wait_for_visibility(MainPageLocators.COOKIE_ACCEPT_BUTTON, timeout=3).click()
        except:
            pass
