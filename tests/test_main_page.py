import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature('Раздел FAQ на главной странице')
class TestFaqSection:

    @pytest.mark.parametrize(
        "question_locator, answer_locator",
        zip(MainPageLocators.FAQ_QUESTIONS, MainPageLocators.FAQ_ANSWERS)
    )
    @allure.title('Проверка отображения ответа на вопрос FAQ')
    @allure.description('Проверяем, что при клике на вопрос в разделе FAQ появляется соответствующий ответ.')
    def test_faq_answers_visible_after_click(self, driver, question_locator, answer_locator):
        with allure.step("Открываем главную страницу"):
            page = MainPage(driver)
            page.open()

        with allure.step("Прокручиваем к вопросу и кликаем по нему"):
            element = page.wait_for_visibility(question_locator)
            page.driver.execute_script("arguments[0].scrollIntoView();", element)
            page.click(question_locator)

        with allure.step("Получаем текст ответа и проверяем, что он не пустой"):
            answer_text = page.get_answer_text(answer_locator)
            assert answer_text != ""
