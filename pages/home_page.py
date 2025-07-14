from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests import conftest


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")
        self.item_inventario = (By.XPATH, "//*[text()='{}']")
        self.adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.abre_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existente(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.adicionar_carrinho)
        self.clicar(self.abre_carrinho)