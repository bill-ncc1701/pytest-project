import conftest

class BasePage:
    def __init__(self):
        self.driver = conftest.driver
        #

    def encontrar_elemento(self, locator):
        # Encontra o elemento na página
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        # Encontra os elementos na página
        return self.driver.find_elements(*locator)

    def clicar(self, locator):
        # Encontra o elemento e clica
        elemento = self.encontrar_elemento(locator)
        elemento.click()

    def escrever(self, locator, texto):
        # Encontra o elemento e escreve o texto
        elemento = self.encontrar_elemento(locator)
        elemento.clear()
        elemento.send_keys(texto)

