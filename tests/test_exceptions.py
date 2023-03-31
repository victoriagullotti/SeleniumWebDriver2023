import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # wait 10 sec or until element is displayed
        wait = WebDriverWait(driver, 10)
        row_2_input_locator = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        # Locate entry field in row #2 with XPath locator
        # $x("//input[@'input-field']") - returns 2 elements type input with class input-field
        # $x("(//input[@class='input-field'])[2]") - returns 1 element type input with class input-field
        # $x("//div[@id='row2']/input") !!!
        #row_2_input_locator =  driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed, but it's not"


    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Wait for the second row to load or until save button is displayed
        wait = WebDriverWait(driver, 10)
        row_2_input_locator = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row_2_input_locator.send_keys("Sushi")

        # Push Save button using locator By.name(“Save”)
        driver.find_element(By.NAME, "Save").click()

        # Verify that text saved
        assert row_2_input_locator.get_attribute("value") == "Test", "Text is not saved"


    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):

        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click adit button
        edit_button_locator = driver.find_element(By.ID, "edit_btn")
        edit_button_locator.click()

        # Clear input field
        row_1_input_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(row_1_input_locator))

        row_1_input_locator.clear() # The element is disabled and may not be manipulated !!! Before we clear the field
        # we need to click on the Edit button !!!

        # Type text into the input field
        row_1_input_locator.send_keys("Some text")

        # Push Save button using locator By.name(“Save”)
        driver.find_element(By.NAME, "Save").click()

        # Verify that comformation message is displayed
        confirmation_message_locator = wait.until(EC.presence_of_element_located((By.ID, "confirmation")))
        assert confirmation_message_locator.is_displayed(), "Confirmation message is not displayed"
