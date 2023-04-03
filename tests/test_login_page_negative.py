import pytest

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    #   Ts1: Verify that error message is displayed when username is incorrect
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("username", "password")
        assert login_page.get_error_message() == expected_error_message, "Error message is not displayed, but it should be"
        assert login_page.is_error_message_displayed(), "Error message is not displayed, but it should be"

    #   Ts2: Verify that error message is displayed when username is incorrect
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("incorrectUser", "Password123")
        assert login_page.get_error_message() == "Your username is invalid!", "Error message is not displayed, but it should be"
        assert login_page.is_error_message_displayed(), "Error message is not displayed, but it should be"

    #   Ts3: Verify that error message is displayed when password is incorrect
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("student", "incorrectPassword")
        assert login_page.get_error_message() == "Your password is invalid!", "Error message is not displayed, but it should be"
        assert login_page.is_error_message_displayed(), "Error message is not displayed, but it should be"

    #   Ts4: Verify that error message is displayed when username and password are incorrect
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username_and_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("incorrectUser", "incorrectPassword")
        assert login_page.get_error_message() == "Your username is invalid!", "Error message is not displayed, but it should be"
        assert login_page.is_error_message_displayed(), "Error message is not displayed, but it should be"
