from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from src.locators.criar_conta_page_locators import CriarContaPageLocators


class CriarContaPageElement:

    def __init__(self, driver):
        self._driver = driver
        self._endereco_completo = None

    def input_account_create(self, nome_primeiro, nome_segundo, senha, rua, cidade, celular, endeco_referencia):
        '''Explicit Waits'''
        '''Para iniciar o preenchimento, após carregar a tela'''
        tempo_seg = 10
        wait = WebDriverWait(self._driver, tempo_seg)
        check_button_mr = wait.until(
            EC.element_to_be_clickable(CriarContaPageLocators.CHECK_BUTTON_MR),
                                        f'Tela de catrastro não carregada em {tempo_seg}seg')
        '''Dados de usuário'''
        check_button_mr.click()
        self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_FIRST_NAME).send_keys(nome_primeiro)
        self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_LAST_NAME).send_keys(nome_segundo)
        self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_PASSWORD).send_keys(senha)
        '''Endereço'''
        self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_ADDRESS).send_keys(rua)
        self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_CITY).send_keys(cidade)

        select = Select(self._driver.find_element(*CriarContaPageLocators.SELECT_TEXT_STATE))
        select.select_by_value('2')
        """obtendo o estado selecionado no formulário'"""
        opcao_selecionada = select.first_selected_option
        estado = opcao_selecionada.text
        cep = '00000'
        self._endereco_completo = rua, cidade, estado, cep
        """"""
        self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_ZIP_POSTAL_CODE).send_keys(cep)
        '''Outros dados'''
        self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_MOBILE_PHONE).send_keys(celular)
        address_reference = self._driver.find_element(*CriarContaPageLocators.INPUT_TEXT_ADDRESS_REFERENCE)
        address_reference.clear()
        address_reference.send_keys(endeco_referencia)
        ''''''
        self._driver.find_element(*CriarContaPageLocators.BUTTON_REGISTER).click()
        ''''''

    def obter_endereco_completo(self):
        return self._endereco_completo
