import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")  # Getting browser from command line!!!
    print(f" Creating {browser} driver")

    #   Create driver based on browser type
    if browser == 'chrome':
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        my_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception(f' Browser {browser} is not supported')

    yield my_driver
    print(f' Closing {browser} driver')
    my_driver.quit()


#   Command line options. This is a hook called by pytest.
#   To run test with firefox: pytest -s -v --browser=firefox tests\test_login_page.py
#   To run test with chrome: pytest -s -v --browser=chrome tests\test_login_page.py
#   To run test with default browser: pytest -s -v tests\test_login_page.py
#   To run test @pytest.mark.login and configuration:
#   -m login --html=reports\report.html --browser=firefox
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Browser to execute test")  # default browser is chrome
