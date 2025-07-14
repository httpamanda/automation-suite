from pages.home_page import HomePage
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup_teardown')
@pytest.mark.login
@pytest.mark.smoke
class TestCT02:
    def test_login_valido(self):

        # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()

        # efetua o login
        login_page.fazer_login_existe("standard_user", "secret_sauce")

        # verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()
        # assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()