from src.page.page_elements.envio_page_elements import EnvioPageElement


class EnvioPage:

    def __init__(self, driver):
        self._driver = driver
        self._page = EnvioPageElement(self._driver)

    def aceitar_termos_e_seguir_para_pagamento(self):
        self._page.go_checkout()

