from src.enum.browsers_enum import BrowsersEnum


class SelectBrowsers:
    """
    Classe que define qual o Browser selecionado para realização da execução
    """
    def __init__(self):
        self._browser = self.browser_selecionado()

    '''Seleção de browser disponivel para execução'''
    @staticmethod
    def browser_selecionado():
        return BrowsersEnum.CHROME

    @property
    def browser_atual(self):
        return self._browser.obter_browser

