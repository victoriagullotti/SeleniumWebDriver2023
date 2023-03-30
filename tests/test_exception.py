import pytest
from selenium.webdriver.common.by import By


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        # wait 2 sec
        time.sleep(2)

        # Verify Row 2 input field is displayed
        # Locate entry field in row #2 with XPath locator
        # $x("//input[@'input-field']") - returns 2 elements type input with class input-field
        # $x("(//input[@class='input-field'])[2]") - returns 1 element type input with class input-field
        # $x("//div[@id='row2']/input") !!!
        row_2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed, but it's not"