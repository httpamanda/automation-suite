import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com/")

    #run
    yield

    # teardown
    driver.quit()