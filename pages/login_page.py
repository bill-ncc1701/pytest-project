from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        # Orgenizando os locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.usuario = "standard_user"
        self.senha = "secret_sauce"

    def fazer_login(self, usuario, senha):
        # Fazendo o Login
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)
