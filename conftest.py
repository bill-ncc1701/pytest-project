import pytest
from selenium import webdriver

driver = webdriver.remote


@pytest.fixture()
def setup_teardown():
    # Setup code
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test => o teste que esta chamando a funcao começa a ser executado a partir daqui.
    yield

    #teardown code
    driver.quit()