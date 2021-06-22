from src.driver.driver_factory import DriverFactory


class BasePage:
    '''
    Classe que contém a url primaria(home) do sistema
    após inicialização do webdriver por outra classe,
    esta determina a url e repassa o webdrive
    '''

    def __init__(self):
        self._url = 'http://automationpractice.com/index.php'
        self._driver = None

    def _obter_driver(self):
        if self._driver is None:
            self._driver = DriverFactory.obter_driver_factory()
            self._driver.get(self._url)
            return self._driver

    def abrir_pagina_base(self):
        self._driver = self._obter_driver()
        return self._driver

