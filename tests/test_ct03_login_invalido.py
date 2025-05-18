import time
import conftest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginInvalido
class TestCT03:
    def test_ct03_login_invalido(self):
        # Fazendo o Login com a senha errada.
        driver = conftest.driver
        #driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #driver.find_element(By.ID, "password").send_keys("senha-incorreta")
        #driver.find_element(By.ID, "login-button").click()

        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce_error")
        assert len(driver.find_elements(By.XPATH,"//span[@class='title']")) == 0

