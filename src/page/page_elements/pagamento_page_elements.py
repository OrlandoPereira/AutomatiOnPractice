from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.pagamento_page_locators import PagamentoPageLocators


class PagamentoPageElement:

    def __init__(self, driver):
        self._driver = driver
        self.button = None


    def check_valor_total(self):
        '''Explicit Waits'''
        '''Para a busca do elemento clicavel, deve que se usar sem o * na busca'''
        tempo_seg = 10
        wait = WebDriverWait(self._driver, tempo_seg)
        self.button = wait.until(
            EC.element_to_be_clickable(PagamentoPageLocators.BUTTON_PAY_BY_BANK_WIRE),
            f'Não achado o botão de checkout em {tempo_seg}seg!')
        return self._driver.find_element(*PagamentoPageLocators.TEXT_COMPRA_TOTAL).text

    def go_payment(self):
        self.button.click()

    def go_confirm_order(self):
        self._driver.find_element(*PagamentoPageLocators.BUTTON_I_CONFIRM_MY_ORDER).click()

    def order_complete(self):
        return self._driver.find_element(*PagamentoPageLocators.TEXT_YOUR_ORDER_ON_MY_STORE_IS_COMPLETE).text

