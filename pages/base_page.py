import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data import TestData


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.base_url = TestData.SCOOTER_URL.rstrip('/')
        self.timeout = timeout

    @allure.step("Открываем страницу: {url}")
    def open(self, url=""):
        if url and not url.startswith('/'):
            url = '/' + url
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

    @allure.step("Скроллим до элемента: {locator}")
    def scroll_to_element(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Ожидаем открытия новой вкладки и переключаемся на нее")
    def wait_and_switch_to_new_tab(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > 1)
        self.switch_to_new_tab()
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != "about:blank")

    @allure.step("Выбираем из выпадающего списка значение: {value}")
    def select_from_dropdown_by_text(self, value, timeout=10):
        locator = (By.XPATH, f'//li[contains(@class, "select-search__row") and contains(normalize-space(), "{value}")]')
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()

    @allure.step('Ожидаем появления элемента: {locator}')
    def wait_for_element(self, locator, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Вводим текст "{text}" в элемент и закрываем всплытие клавишей Escape')
    def input_text_and_escape(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ESCAPE)
