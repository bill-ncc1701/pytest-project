import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import driver

@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_login_invalido(self):
        # Fazendo o Login com a senha errada.
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("senha-incorreta")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        assert not driver.find_element(By.XPATH,"//span[@class='title']").is_displayed()

