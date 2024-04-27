from selenium.webdriver.common.by import By
import time

class Urls:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru'
    ORDER_PAGE = '/order'
    LINK_YANDEX = 'https://dzen.ru/?yredirect=true'
    LINK_SAMOCAT = 'https://qa-scooter.praktikum-services.ru/'



class Test_data_questions:

    TEST_DATA = [
        ['0', '0', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        ['1', '1', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        ['2', '2',
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        ['3', '3',
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        ['4', '4',
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        ['5', '5',
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        ['6', '6',
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        ['7', '7', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
    ]


class Data_order:
    '''TEST_DATA_USER = [
    ["Катя","Катина","Москва улица Тверская 7",(By.XPATH, '//li[@class = "select-search__row"]//div[text()="Черкизовская"]'),"89321112233","23.04.2024",(By.XPATH, '//div[@class = "Dropdown-option"][text()="сутки"]'),(By.XPATH, '//input[@id = "black"]'),"Все Супер",],
    ["Иван","Иванов","Москва улица 50 лет Октября 60",(By.XPATH, '//li[@class = "select-search__row"]//div[text()="Комсомольская"]'),"89332221144","24.04.2024",(By.XPATH, '//div[@class = "Dropdown-option"][text()="двое суток"]'), (By.XPATH, '//input[@id = "grey"]'), "Спасибо!"]
    ]'''
    TEST_DATA_USER = [
        ["Катя", "Катина", "Москва улица Тверская 7",
         "Черкизовская", "89321112233", "23.04.2024", "сутки", "black","Все Супер"],
        ["Иван", "Иванов", "Москва улица 50 лет Октября 60",
         "Комсомольская", "89332221144", "24.04.2024", "двое суток", "grey", "Спасибо!"]
    ]


