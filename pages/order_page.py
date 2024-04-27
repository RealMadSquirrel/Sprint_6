import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполняем имя')
    def set_name(self, name):
        self.find_element_and_send_keys(OrderPageLocators.NAME, name)

    @allure.step('Заполняем фамилию')
    def set_surname(self, surname):
        self.find_element_and_send_keys(OrderPageLocators.SURNAME, surname)

    @allure.step('Заполняем адрес')
    def set_address(self, address):
        self.find_element_and_send_keys(OrderPageLocators.ADDRESS, address)

    @allure.step('Устанавливаем станцию метро')
    def set_metro_station(self, station):
        metro = self.wait_and_find_element(OrderPageLocators.METRO)
        metro.click()
        metro_station = self.wait_and_find_element(station)
        metro_station.click()

    @allure.step('Заполняем телефон')
    def set_phone(self, phone):
        self.find_element_and_send_keys(OrderPageLocators.PHONE, phone)

    @allure.step('Заполняем дату, когда привести самокат')
    def set_date(self, date):
        self.find_element_and_send_keys(OrderPageLocators.DATE, date)
        self.find_element_and_send_keys(OrderPageLocators.DATE, Keys.ENTER)

    @allure.step('Заполняем срок аренды')
    def set_time_rent(self, time_rent):
        self.click(OrderPageLocators.TIME_RENT)
        self.click(time_rent)

    @allure.step('Заполняем комментарий')
    def set_comment(self, comment):
        self.find_element_and_send_keys(OrderPageLocators.COMMENT, comment)


