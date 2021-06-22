from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.pedido_page_locators import PedidosPageLocators


class PedidoPageElement:

    def __init__(self, driver):
        self._driver = driver


    def check_pedido(self, produto_name):
        '''Explicit Waits'''
        '''Para a busca do elemento nome do produto, deve se usar sem o * na busca'''
        wait = WebDriverWait(self._driver, 5)
        element = wait.until(
            EC.text_to_be_present_in_element(PedidosPageLocators.TEXT_NAME_PRODUCT_1, produto_name))

        return element

    def check_valor_total(self):
        return self._driver.find_element(*PedidosPageLocators.TEXT_COMPRA_TOTAL).text

    def go_order(self):
        self._driver.find_element(*PedidosPageLocators.BUTTON_PROCEEED_TO_CHECKOUT).click()
