from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def open_page(self, url):
        self.driver.get(url)

    def get_cookie(self, url):
        self.driver.get_cookies()

    def find_element_and_send_keys(self, locator, key):
        return self.driver.find_element(*locator).send_keys(*key)

    def click(self, locator):
        return self.driver.find_element(*locator).click()

    def url_changes(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_changes(url))

    def url_to_be(self, url):
        return WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    def click_and_hold(self,locator):
        clickable = self.driver.find_element(By.ID, "clickable")
        ActionChains(driver).click_and_hold(clickable).perform()
