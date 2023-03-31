class LoggedInSuccessfully:
    __ulr = "http://the-internet.herokuapp.com/secure"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_logout(self):
        self.driver.find_element_by_link_text("Log out").click()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_logout(self):
        self.driver.find_element_by_link_text("Log out").click()