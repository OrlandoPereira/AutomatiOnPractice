from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.endereco_entrega_locators import EnderecoDeEntregaPageLocators


class EnderecoDeEntregaPageElement:

    def __init__(self, driver):
        self._driver = driver

    def go_shipping(self):
        self._driver.find_element(*EnderecoDeEntregaPageLocators.BUTTON_PROCEED_TO_CHECKOUT).click()


    def check_endereco(self):
        '''Explicit Waits'''
        '''Para iniciar o validaçao, após carregar a tela'''
        tempo_seg = 10
        wait = WebDriverWait(self._driver, tempo_seg)
        text_your_delivery_address = wait.until(
            EC.text_to_be_present_in_element(EnderecoDeEntregaPageLocators.TEXT_YOUR_DELIVERY_ADDRESS,
                                             'YOUR DELIVERY ADDRESS'),
                                        f'Tela de validação de endereço não carregada em {tempo_seg}seg')

        rua = self._driver.find_element(*EnderecoDeEntregaPageLocators.TEXT_ADDRESS).text
        cidade_estado_cep = self._driver.find_element(*EnderecoDeEntregaPageLocators.TEXT_CITY_STATE_POSTCODE).text

        return rua, cidade_estado_cep


