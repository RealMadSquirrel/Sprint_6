import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Прокрутка страницы до конца страницы')
    def scroll_to_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Прокрутка страницы с заданным значением пикселей')
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.wait_and_find_element(locator))

    @allure.step('Кликаем на элемент с ожиданием')
    def wait_and_click_to_element(self, locator):
        button = self.wait_and_find_element(locator)
        button.click()


