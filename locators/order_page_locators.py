import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class OrderPageLocators:
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

    @allure.step('Формируем локатор для станции метро')
    def get_locators_station(station):
        LOCATOR_STATION = [By.XPATH, "//li[@class = 'select-search__row']//div[text()='" + station + "']"]
        return LOCATOR_STATION

    @allure.step('Формируем локатор для время аренды')
    def get_locators_time_rent(time_rent):
        LOCATOR_RENT = [By.XPATH, "//div[@class = 'Dropdown-option'][text()='" + time_rent + "']"]
        return LOCATOR_RENT

    @allure.step('Формируем локатор для время аренды')
    def get_locators_color(color):
        LOCATOR_COLOR = [By.XPATH, "//input[@id = '" + color + "']"]
        return LOCATOR_COLOR
