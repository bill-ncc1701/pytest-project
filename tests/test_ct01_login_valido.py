import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import conftest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.loginValido
@pytest.mark.smoke
class TestCT01:
    def test_ct01_login_valido(self):
        # Fazendo o Login
        driver = conftest.driver
        # driver.find_element(By.ID, "user-name").send_keys("standard_user")
        # driver.find_element(By.ID, "password").send_keys("secret_sauce")
        # driver.find_element(By.ID, "login-button").click()
        # time.sleep(2)
        login_page = LoginPage()
        login_page.fazer_login("standard_user","secret_sauce")

        assert driver.find_element(By.XPATH,"//span[@class='title']").is_displayed()

