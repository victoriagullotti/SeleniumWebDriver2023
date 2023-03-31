from selenium.webdriver.chrome.webdriver import WebDriver


class LoginPage:

    # Private variables
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")

    # Constructor
    def __init__(self, driver: WebDriver):
        self._driver = driver

    # Public methods
    def open(self):
        self.driver.get(self.__url)

def execute_login(driver, username, password):

    # 1 wait for all elements to be present!!!
    wait = WebDriverWait(self._driver, 10)
    wait.until(EC.presence_of_element_located(self.__username_field))
    wait.until(EC.presence_of_element_located(self.__password_field))
    wait.until(EC.presence_of_element_located(self.__submit_button))

    # 2 Send keys to username and password fields
    self._driver.find_element(*self.__username_field).send_keys(username)

    self._driver.find_element(*self.__password_field).send_keys(password)

    self._driver.find_element(*self.__submit_button).click()