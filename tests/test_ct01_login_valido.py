import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import driver

@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_login_valido(self):
        # Fazendo o Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,"//span[@class='title']").is_displayed()

