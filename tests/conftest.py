from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import pytest


#   Fixture
@pytest.fixture()
def driver():
    print("Creating chrome driver")
    my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    print("Closing chrome driver")
    my_driver.quit()
