from faker import Faker
from src.page.page_elements.criar_conta_page_elements import CriarContaPageElement


class CriarContaPage:

    def __init__(self, driver):
        self._driver = driver
        self.faker = Faker('pt_BR')
        self._page = CriarContaPageElement(self._driver)

    def criar_nova_conta(self):
        '''Dados para o cadastro gerados aleatóriamente'''
        '''Dados de usuário'''
        nome_primeiro = self.faker.first_name()
        nome_segundo = self.faker.last_name()
        senha = self.faker.swift8()
        '''Dados de endereço'''
        rua = self.faker.street_address()
        cidade = self.faker.city()
        '''Outros Dados'''
        celular = self.faker.cellphone_number()
        endeco_referencia = self.faker.street_address()

        self._page.input_account_create(nome_primeiro, nome_segundo, senha, rua, cidade, celular, endeco_referencia)


    def endereco_completo_do_cadastro(self):
        return self._page.obter_endereco_completo()

