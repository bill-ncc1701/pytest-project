from selenium.webdriver.common.by import By
import conftest

class LoginPage:
    def __init__(self):
        self.driver = conftest.driver
        # Orgenizando os locators
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        # Fazendo o Login
        # driver = conftest.driver
        self.driver.find_element(*self.username).send_keys(usuario)
        self.driver.find_element(*self.password).send_keys(senha)
        self.driver.find_element(*self.login_button).click()
