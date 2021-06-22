from src.page.page_elements.produto_page_elements import ProdutoPageElement


class ProdutoPage:

    def __init__(self, driver):
        self._driver = driver
        self._page = ProdutoPageElement(self._driver)

    def adicionar_produto_ao_pedido(self):
        self._page.add_carinho()

    def ir_checkout(self):
        self._page.go_checkout()

    def nome_produto_selecionado(self):
        return self._page.obter_nome_produto_selecionado()


