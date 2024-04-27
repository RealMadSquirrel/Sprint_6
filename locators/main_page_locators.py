import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class MainPageLocators:
    LOCATOR_TO_QUESTION = (By.XPATH, "//div[text() = 'Вопросы о важном']")
    LOCATOR_COOKIE = (By.XPATH, "//*[@id='rcc-confirm-button']")
    BUTTON_ORDER_UP = (By.XPATH, "//button[text() = 'Заказать']")  # кнопка Заказать верхняя
    BUTTON_ORDER_DOWN = (By.XPATH,".//div[contains(@class,'Home_FinishButton')]/button[contains(text(),'Заказать')]")  # кнопка Заказать нижняя
    TITLE_FORM_1 = (By.XPATH, "//div[text() = 'Для кого самокат']")  # локатор для проверкb перехода к форме заполнения заказа №1

    LINK_YANDEX = (By.XPATH, "//a[contains(@href,'//yandex.ru')]")
    LINK_SAMOCAT = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")

    @allure.step('Формируем локатор для вопроса')
    def get_locators_questions(number):
        LOCATOR_QUESTION = [By.XPATH, "//*[@id='accordion__heading-" + number + "']"]
        return LOCATOR_QUESTION

    @allure.step('Формируем локатор для ответа')
    def get_locator_answer(number):
        LOCATOR_ANSWER = [By.XPATH, "//*[@id='accordion__panel-" + number + "']/p"]
        return LOCATOR_ANSWER
