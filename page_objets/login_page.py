from selenium.webdriver.chrome.webdriver import WebDriver

from page_objets.base_page import BasePage


class LoginPage(BasePage):

    # Private variables
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")

    # Constructor
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # Public methods
    def open(self):
        super().open(self.__url)

    def execute_login(driver, username, password):

        super._type(self.__username_field, username)
        super._type(self.__password_field, password)
        super._click(self.__submit_button)

