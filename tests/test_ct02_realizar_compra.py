# Fazer o Login
import time
import pytest
import conftest
from selenium.webdriver.common.by import By



from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.realizarCompra
@pytest.mark.smoke
class TestCT02:
    def test_ct02_realizar_compra(self):
        # Realizando uma compra no site
        driver = conftest.driver

        #driver.find_element(By.ID, "user-name").send_keys("standard_user")
        #driver.find_element(By.ID, "password").send_keys("secret_sauce")
        #driver.find_element(By.ID, "login-button").click()

        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_sauce")

        # Wait for the alert to appear (you might need to adjust the time based on your page load time)
        time.sleep(5)

        #Alert(driver).accept()

        # Escolher o produto
        driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Backpack']").click()

        time.sleep(2)
        # Adicionar o produto ao carrinho
        driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
        # Verificar se o produto foi adicionado ao carrinho
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

        #Voltando para a lista de produtos
        driver.find_element(By.XPATH,"//button[@class='btn btn_secondary back btn_medium']").click()

        #Escolhendo a blusa Laranja

        # Escolher o produto
        driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Test.allTheThings() T-Shirt (Red)']").click()

        time.sleep(2)
        # Adicionar o produto ao carrinho
        driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
        # Verificar se o produto foi adicionado ao carrinho
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        #Voltando para a lista de produtos
        driver.find_element(By.XPATH,"//button[@class='btn btn_secondary back btn_medium']").click()

        #Escolhendo o macacão para Bebẽ
        driver.find_element(By.XPATH,"//*[@class='inventory_item_name ' and text()='Sauce Labs Onesie']").click()

        time.sleep(2)
        # Adicionar o produto ao carrinho
        driver.find_element(By.XPATH,"//*[text()='Add to cart']").click()
        # Verificar se o produto foi adicionado ao carrinho
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(2)

        #Conluir a compra (CHECKOUT)
        driver.find_element(By.XPATH,"//button[@class='btn btn_action btn_medium checkout_button ']").click()

        #Preenchendo os dados do checkout
        first_name = "Willian"
        last_name = "Cevassi"
        postal_code = "86828-000"

        driver.find_element(By.ID,"first-name").send_keys(first_name)
        driver.find_element(By.ID,"last-name").send_keys(last_name)
        driver.find_element(By.ID,"postal-code").send_keys(postal_code)

        #clicar no botão CONTINUAR
        driver.find_element(By.ID,"continue").click()

        #Testando se caiu na tela final
        assert driver.find_element(By.XPATH,"//*[@class='header_secondary_container']").is_displayed() , "Não foi possível encontrar a tela de checkout"

        #Finalizando a compra
        driver.find_element(By.ID, "finish").click()

        #Testa se caiu na tela de finalização
        assert driver.find_element(By.XPATH,"//h2[@class='complete-header' ]").is_displayed() , "Não foi possível encontrar a tela de finalização"
