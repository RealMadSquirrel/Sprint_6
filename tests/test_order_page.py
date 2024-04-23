import allure
import pytest
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Urls
from data import Test_data_questions
from data import Data_order


class TestOrder:

    @allure.title("Проверка заполнения форм с разными наборами данных")
    @pytest.mark.parametrize(
        'name, surname, address, station, phone,date, time_rent, color, comment', Data_order.TEST_DATA_USER
    )
    def test_fill_form_order(self, driver, name, surname, address, station, phone, date, time_rent, color, comment):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE)
        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_address(address)
        order_page.set_metro_station(station)
        order_page.set_phone(phone)

        order_page.click(OrderPage.BUTTON_NEXT)

        order_page.set_date(date)
        order_page.set_time_rent(time_rent)
        order_page.click(color)
        order_page.set_comment(comment)
        order_page.click(OrderPage.ORDER_BUTTON)
        order_page.click(OrderPage.ORDER_BUTTON_YES)

        assert 'Заказ оформлен' in order_page.wait_and_find_element(OrderPage.ORDER_FORM_SUCCESS).text
