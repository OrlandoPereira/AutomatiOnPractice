from src.page.page_elements.home_page_elements import HomePageElement

class HomePage:

    def __init__(self, driver):
        self._driver = driver
        self._page = HomePageElement(self._driver)

    def clicar_produto_1(self):
        self._page.clic_produto_1()


