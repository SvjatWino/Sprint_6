import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from data import TestData


@allure.feature('Раздел FAQ на главной странице')
class TestFaqSection:

    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_text",
        [
            (q, a, t) for (q, a), (_, t) in zip(
                zip(MainPageLocators.FAQ_QUESTIONS, MainPageLocators.FAQ_ANSWERS),
                TestData.QUESTIONS_AND_ANSWERS
            )
        ]
    )
    @allure.title('Проверка отображения ответа на вопрос FAQ')
    @allure.description('Проверяем, что при клике на вопрос в разделе FAQ появляется соответствующий ответ.')
    def test_faq_answers_visible_after_click(self, driver, question_locator, answer_locator, expected_text):
        page = MainPage(driver)

        with allure.step("Открываем главную страницу"):
            page.open()

        with allure.step("Прокручиваем к вопросу и кликаем по нему"):
            page.scroll_to_element(question_locator)
            page.click(question_locator)

        with allure.step("Получаем текст ответа и проверяем соответствие ожидаемому"):
            answer_text = page.get_answer_text(answer_locator)
            assert answer_text == expected_text, f"Ожидалось: '{expected_text}', получено: '{answer_text}'"
