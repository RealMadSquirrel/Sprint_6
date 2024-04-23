from selenium.webdriver.common.by import By


class Urls:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    LINK_YANDEX = 'https://dzen.ru/?yredirect=true'
    LINK_SAMOCAT = 'https://qa-scooter.praktikum-services.ru/'



class Test_data_questions:
    TEST_DATA = [
        [(By.XPATH, "//*[@id='accordion__heading-0']"), (By.XPATH, "//*[@id='accordion__panel-0']/p"),
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
        [(By.XPATH, "//*[@id='accordion__heading-1']"), (By.XPATH, "//*[@id='accordion__panel-1']/p"),
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
        [(By.XPATH, "//*[@id='accordion__heading-2']"), (By.XPATH, "//*[@id='accordion__panel-2']/p"),
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
        [(By.XPATH, "//*[@id='accordion__heading-3']"), (By.XPATH, "//*[@id='accordion__panel-3']/p"),
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
        [(By.XPATH, "//*[@id='accordion__heading-4']"), (By.XPATH, "//*[@id='accordion__panel-4']/p"),
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [(By.XPATH, "//*[@id='accordion__heading-5']"), (By.XPATH, "//*[@id='accordion__panel-5']/p"),
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
        [(By.XPATH, "//*[@id='accordion__heading-6']"), (By.XPATH, "//*[@id='accordion__panel-6']/p"),
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [(By.XPATH, "//*[@id='accordion__heading-7']"), (By.XPATH, "//*[@id='accordion__panel-7']/p"),
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
    ]

class Data_order:
    TEST_DATA_USER = [
    ["Катя","Катина","Москва улица Тверская 7",(By.XPATH, '//li[@class = "select-search__row"]//div[text()="Черкизовская"]'),"89321112233","23.04.2024",(By.XPATH, '//div[@class = "Dropdown-option"][text()="сутки"]'),(By.XPATH, '//input[@id = "black"]'),"Все Супер",],
    ["Иван","Иванов","Москва улица 50 лет Октября60",(By.XPATH, '//li[@class = "select-search__row"]//div[text()="Комсомольская"]'),"89332221144","24.04.2024",(By.XPATH, '//div[@class = "Dropdown-option"][text()="двое суток"]'), (By.XPATH, '//input[@id = "grey"]'), "Спасибо!"]
    ]



