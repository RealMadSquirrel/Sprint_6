import time

import allure
import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from data import Urls
from data import Test_data_questions
from locators.main_page_locators import MainPageLocators


class TestQuestionsMainPage:

    @allure.title("Проверка Вопросов о важном")
    @allure.description("При нажатии на стрелочку, открывается соответствующий ответ")
    @pytest.mark.parametrize(
        'locator_questions, locator_answer, answer', Test_data_questions.TEST_DATA
    )
    def test_questions(self, driver, locator_questions, locator_answer, answer):
        questions_page = MainPage(driver)
        questions_page.open_page(Urls.MAIN_PAGE)
        questions_page.wait_and_click_to_element(MainPageLocators.LOCATOR_COOKIE)
        questions_page.scroll_to_end()
        questions_page.wait_and_click_to_element(MainPageLocators.get_locators_questions(locator_questions))
        assert questions_page.wait_and_find_element(MainPageLocators.get_locator_answer(locator_answer)).text == answer


class TestClickOrderMainPage:
    @allure.title("Проверка клика на кнопку Заказать сверху")
    def test_click_order_up(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.wait_and_click_to_element(MainPageLocators.BUTTON_ORDER_UP)
        assert main_page.wait_and_find_element(MainPageLocators.TITLE_FORM_1).text == 'Для кого самокат'

    @allure.title("Проверка клика на кнопку Заказать снизу")
    def test_click_order_down(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.wait_and_click_to_element(MainPageLocators.LOCATOR_COOKIE)
        main_page.scroll_to_element(MainPageLocators.BUTTON_ORDER_DOWN)
        main_page.wait_and_click_to_element(MainPageLocators.BUTTON_ORDER_DOWN)
        assert main_page.wait_and_find_element(MainPageLocators.TITLE_FORM_1).text == 'Для кого самокат'


class TestLogoMainPage:
    @allure.title(
        "Проверка,что при нажатии на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.")
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.wait_and_click_to_element(MainPageLocators.LOCATOR_COOKIE)
        main_page.click(MainPageLocators.LINK_YANDEX)
        assert main_page.url_changes(Urls.LINK_YANDEX)

    @allure.title(
        "Проверка,что при нажатии на логотип «Самоката», попадёшь на главную страницу «Самоката».")
    def test_logo_samocat(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.wait_and_click_to_element(MainPageLocators.LOCATOR_COOKIE)
        main_page.click(MainPageLocators.LINK_SAMOCAT)
        assert main_page.url_to_be(Urls.LINK_SAMOCAT)
