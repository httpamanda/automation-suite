import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from . import conftest
import pdb

@pytest.mark.usefixtures('setup_teardown')
class TestCT01:
    def test_adicionar_produtos_carrinho(self):
        driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        pdb.set_trace()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Ligswssht"
        assert produto_2 == "Sauce Labs Bike Light"

        
        # efetua o login
        login_page.fazer_login("standard_user", "secret_sauce")

        # adiciona item ao carrinho e abre o carrinho
        home_page.adicionar_ao_carrinho(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # volta a pagina inicial
        carrinho_page.clicar_continuar_comprando()

        # adiciona mais itens e abre o carrinho
        home_page.adicionar_ao_carrinho(produto_2)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)