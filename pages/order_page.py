import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME = (By.CSS_SELECTOR, '[placeholder="* Имя"]')
    SURNAME = (By.CSS_SELECTOR, '[placeholder="* Фамилия"]')
    ADDRESS = (By.CSS_SELECTOR, '[placeholder="* Адрес: куда привезти заказ"]')
    METRO = (By.CSS_SELECTOR, '[placeholder="* Станция метро"]')
    PHONE = (By.CSS_SELECTOR, '[placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_NEXT = (By.XPATH, "//button[text() = 'Далее']")

    DATE = (By.CSS_SELECTOR, '[placeholder="* Когда привезти самокат"]')
    TIME_RENT = (By.XPATH, '//div[@class = "Dropdown-placeholder"]')
    COMMENT = (By.CSS_SELECTOR, '[placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class,'Order_Buttons')]/button[contains(text(),'Заказать')]")
    ORDER_BUTTON_YES = (By.XPATH, ".//div[contains(@class,'Order_Buttons')]/button[contains(text(),'Да')]")
    ORDER_FORM_SUCCESS = (By.XPATH, ".//div[contains(text(),'Заказ оформлен')]")

    @allure.step('Заполняем имя')
    def set_name(self, name):
        self.find_element_and_send_keys(self.NAME, name)

    @allure.step('Заполняем фамилию')
    def set_surname(self, surname):
        self.find_element_and_send_keys(self.SURNAME, surname)

    @allure.step('Заполняем адрес')
    def set_address(self, address):
        self.find_element_and_send_keys(self.ADDRESS, address)

    @allure.step('Устанавливаем станцию метро')
    def set_metro_station(self, station):
        metro = self.wait_and_find_element(self.METRO)
        metro.click()
        metro_station = self.wait_and_find_element(station)
        metro_station.click()

    @allure.step('Заполняем телефон')
    def set_phone(self, phone):
        self.find_element_and_send_keys(self.PHONE, phone)

    @allure.step('Заполняем дату, когда привести самокат')
    def set_date(self, date):
        self.find_element_and_send_keys(self.DATE, date)
        self.find_element_and_send_keys(self.DATE, Keys.ENTER)

    @allure.step('Заполняем срок аренды')
    def set_time_rent(self, time_rent):
        self.click(self.TIME_RENT)
        self.click(time_rent)

    @allure.step('Заполняем комментарий')
    def set_comment(self, comment):
        self.find_element_and_send_keys(self.COMMENT, comment)








