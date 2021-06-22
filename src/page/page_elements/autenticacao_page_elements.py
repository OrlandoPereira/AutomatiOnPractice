from src.locators.autenticacao_page_locators import AutenticacaoPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutenticacaoPageElement:

    def __init__(self, driver):
        self._driver = driver

    def input_email_create(self, emailAddress):
        '''Explicit Waits'''
        '''Para iniciar o preenchimento, após carregar a tela'''
        tempo_seg = 10
        wait = WebDriverWait(self._driver, tempo_seg)
        button_create = wait.until(
            EC.element_to_be_clickable(AutenticacaoPageLocators.BUTTON_CREATE_AN_ACCOUNT),
                                        f'Tela de autenticaçao não carregada em {tempo_seg}seg')

        email_input = self._driver.find_element(*AutenticacaoPageLocators.INPUT_TEXT_EMAIL_CREATE)
        email_input.send_keys(emailAddress)
        button_create.click()
