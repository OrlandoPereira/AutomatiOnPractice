from src.locators.home_page_locators import HomePageLocators

class HomePageElement:

    def __init__(self, driver):
        self._driver = driver

    def clic_produto_1(self):
        self._driver.find_element(*HomePageLocators.produto_model_1).click()

