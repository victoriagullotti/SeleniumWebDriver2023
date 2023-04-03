from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    @property
    def _url(self) -> str:
        return self.driver.current_url

    def __init__(self, driver: webdriver):
        self.driver = driver

    def _find_element(self, locator: tuple):
        return self.driver.find_element(*locator)  # * is used to unpack the tuple !!!

    def _type(self, locator: tuple, text: str):
        self._wait_for_element_to_be_visible(locator)
        self._find_element(locator).send_keys(text)

    def _click(self, locator: tuple):
        self._wait_for_element_to_be_clickable(locator)
        self._find_element(locator).click()

    def _wait_for_element_to_be_clickable(self, locator: tuple, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def _wait_for_element_to_be_visible(self, locator: tuple, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find_element(locator).is_displayed()

        # If the element is not found, the exception is caught and the method returns False
        except NoSuchElementException:
            return False

    def open_url(self, url: str):
        self.driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:

        return self._find_element(locator).text # returns the text of the element