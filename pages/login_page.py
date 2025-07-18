from pages.base_page import BasePage
from tests import conftest
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button_field = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//*[@data-test='error']")

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button_field)

    def verificar_mensagem_erro_login_existe(self):
        self.verificar_se_elemento_existente(self.error_message_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto retornado foi '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'"