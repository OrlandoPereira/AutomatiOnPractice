from src.page.page_elements.pagamento_page_elements import PagamentoPageElement


class PagamentoPage:

    def __init__(self, driver):
        self._driver = driver
        self._page = PagamentoPageElement(self._driver)

    def verificar_valor_total_da_compra_em_pagamento(self, total_anunciado):
        total_caixa = self._page.check_valor_total()
        if total_caixa == total_anunciado:
            return True
        return False

    def pagamento_por_transferencia_bancaria(self):
        self._page.go_payment()

    def confirmar_pagamento(self):
        self._page.go_confirm_order()

    def confirmar_pedido_concluido(self):
        return self._page.order_complete()
