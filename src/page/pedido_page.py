from src.page.page_elements.pedido_page_elements import PedidoPageElement


class PedidoPage:

    def __init__(self, driver):
        self._driver = driver
        self._page = PedidoPageElement(self._driver)

    def nome_produto_selecionado(self, produto_name):
        return self._page.check_pedido(produto_name)

    def valor_Total_compra(self):
        return self._page.check_valor_total()

    def seguir_com_a_compra(self):
        self._page.go_order()
