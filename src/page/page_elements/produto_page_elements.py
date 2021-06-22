from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.produto_page_locators import ProdutoPageLocators


class ProdutoPageElement:

    def __init__(self, driver):
        self._driver = driver
        self._produto = None


    def add_carinho(self):
        self._produto = self._driver.find_element(*ProdutoPageLocators.TEXT_NAME_PRODUCT).text
        self._driver.find_element(*ProdutoPageLocators.BUTTON_ADD_TO_CART).click()


    def go_checkout(self):
        '''Explicit Waits'''
        '''Para a busca do elemento clicavel, deve que se usar sem o * na busca'''
        tempo_seg = 10
        wait = WebDriverWait(self._driver, tempo_seg)
        element = wait.until(
            EC.element_to_be_clickable(ProdutoPageLocators.BUTTON_PROCEEED_TO_CHECKOUT),
            f'Não achado o botão de checkout em {tempo_seg}seg!')
        element.click()

    def obter_nome_produto_selecionado(self):
        return self._produto
