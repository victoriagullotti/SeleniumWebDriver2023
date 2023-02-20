import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    def test_negative_username(self):
        @pytest.mark.login
        @pytest.mark.negative
        def test_positive_login(self):
            #   Create Chrom driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
            time.sleep(5)  # Sleep 5 sec

            #   Open browser
            driver.get('https://practicetestautomation.com/practice-test-login/')

            #   Type username
            username_locator = driver.find_element(By.ID, 'username')
            username_locator.send_keys('khcljc')

            #   Type password
            password_locator = driver.find_element(By.NAME, 'password')
            password_locator.send_keys("Password123")

            #   Submit button. Xpath locator $x("//button[@class='btn']")
            submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
            submit_button_locator.click()
            time.sleep(3)

            #   Error
            error_message_locator = driver.find_element(By.ID, "error")
            assert error_message_locator.is_displayed(), "Error message is nor displayed"

            error_message_text = error_message_locator.text
            assert error_message_text == "Your user name is invalid", "Wrong error message"
