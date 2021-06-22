from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.envio_page_locators import EnvioPageLocators


class EnvioPageElement:

    def __init__(self, driver):
        self._driver = driver


    def go_checkout(self):
        '''Explicit Waits'''
        '''Para a busca do elemento clicavel, deve que se usar sem o * na busca'''
        tempo_seg = 10
        wait = WebDriverWait(self._driver, tempo_seg)
        button = wait.until(
            EC.element_to_be_clickable(EnvioPageLocators.BUTTON_PROCEEED_TO_CHECKOUT),
            f'Não achado o botão de checkout em {tempo_seg}seg!')
        self._driver.find_element(*EnvioPageLocators.CHECK_TERMS_OF_SERVICE).click()
        button.click()

