from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import conftest

class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//*[text()='{}']")
        self.botao_continuar_comprando = (By.XPATH, "//*[@id='continue-shopping']")

    def verificar_produto_carrinho_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existente(item)

    def clicar_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)