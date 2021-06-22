from faker import Faker
from src.page.page_elements.autenticacao_page_elements import AutenticacaoPageElement


class AutenticacaoPage:

    def __init__(self, driver):
        self._driver = driver
        self.faker = Faker('pt_BR')
        self._page = AutenticacaoPageElement(self._driver)

    def entrar_nova_conta(self):
        self._page.input_email_create(self.faker.ascii_free_email())


