
from src.page.page_elements.endereco_entrega_elements import EnderecoDeEntregaPageElement


class EnderecoDeEntregaPage:

    def __init__(self, driver):
        self._driver = driver
        self._page = EnderecoDeEntregaPageElement(self._driver)

    def verificar_endereco_entrega(self, endereco_completo):
        endereco_entrega = self._page.check_endereco()
        endereco_completo = endereco_completo[0], f'{endereco_completo[1]}, {endereco_completo[2]} {endereco_completo[3]}'

        if endereco_entrega == endereco_completo:
            return True
        return False

    def seguir_para_frete(self):
        self._page.go_shipping()

