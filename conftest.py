import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()
