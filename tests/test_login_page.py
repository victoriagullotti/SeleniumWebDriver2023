import time

import pytest
from selenium.webdriver.common.by import By


class TestPositiveScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        #   Create Chrome driver
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #time.sleep(5)  # Sleep 5 sec

        #   Open browser
        driver.get('https://practicetestautomation.com/practice-test-login/')

        time.sleep(5)  # Sleep 5 sec

        #   Type username
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys('student')

        #   Type password
        password_locator = driver.find_element(By.NAME, 'password')
        password_locator.send_keys("Password123")

        #   Submit button. Xpath locator $x("//button[@class='btn']")
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(3)

        # Verify URL
        page_url = driver.current_url
        assert page_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Text locator
        text_locator = driver.find_element(By.TAG_NAME, 'h1')
        actual_text = text_locator.text
        assert actual_text == "Logged In Successfully"

        #   Link
        log_out_button = driver.find_element(By.LINK_TEXT, 'Log out')
        assert log_out_button.is_displayed()
