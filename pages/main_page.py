import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    LOCATOR_TO_QUESTION = (By.XPATH, "//div[text() = 'Вопросы о важном']")
    LOCATOR_COOKIE = (By.XPATH, "//*[@id='rcc-confirm-button']")
    BUTTON_ORDER_UP  = (By.XPATH, "//button[text() = 'Заказать']") #кнопка Заказать верхняя
    BUTTON_ORDER_DOWN = (By.XPATH, ".//div[contains(@class,'Home_FinishButton')]/button[contains(text(),'Заказать')]") #кнопка Заказать нижняя
    TITLE_FORM_1 = (By.XPATH, "//div[text() = 'Для кого самокат']") #локатор для проверка перехода к форме заполнения заказала №1

    LINK_YANDEX = (By.XPATH, "//a[contains(@href,'//yandex.ru')]")
    LINK_SAMOCAT = (By.XPATH, "//a[contains(@class,'Header_LogoScooter')]")

    @allure.step('Прокрутка страницы до конца страницы')
    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Прокрутка страницы с заданным значением пикселей')
    def scroll_to_element(self):
        self.driver.execute_script("window.scrollTo(0, 1800)")

    @allure.step('Кликаем на Вопрос')
    def click_to_questions_button(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step('Убираем куки')
    def click_to_cookie(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()

    @allure.step('Нажимаем на кнопку Заказать')
    def click_to_order(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()




