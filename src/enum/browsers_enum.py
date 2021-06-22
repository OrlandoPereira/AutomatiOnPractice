from enum import Enum, auto


class BrowsersEnum(Enum):
    CHROME = auto()
    FIREFOX = auto()

    @property
    def obter_browser(self):
       if self == self.CHROME:
           self._opcao = self.CHROME.name
       elif self == self.FIREFOX:
           self._opcao = self.FIREFOX.name
       return self._opcao
