from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_personal_info(self, first_name, last_name, address, metro, phone):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).send_keys(metro)
        metro_option = (By.XPATH, f'//li[@class="select-search__row" and contains(text(), "{metro}")]')
        self.wait.until(EC.visibility_of_element_located(metro_option)).click()
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_order_info(self, date, comment, color='black', rent_period='сутки'):
        self.driver.find_element(*OrderPageLocators.DATE_INPUT).send_keys(date)
        self.driver.find_element(*OrderPageLocators.RENT_DROPDOWN).click()

        rent_option = OrderPageLocators.RENT_OPTIONS[rent_period]
        self.driver.find_element(*rent_option).click()

        if color == 'black':
            self.driver.find_element(*OrderPageLocators.COLOR_BLACK).click()
        elif color == 'grey':
            self.driver.find_element(*OrderPageLocators.COLOR_GREY).click()

        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    def submit_order(self):
        self.driver.find_element(*OrderPageLocators.ORDER_SUBMIT_BUTTON).click()
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)).click()

    def order_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL)
        ).is_displayed()

