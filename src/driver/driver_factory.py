from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from src.util.switch import Switch
from src.param.select_browser import SelectBrowsers

class DriverFactory:
    '''
    Classe responsavel por verificar qual navegador será executado e
    fazer a inicialização do webdriver com o navegador correto do ambiente
    '''
    @staticmethod
    def obter_driver_factory():
            Switch(SelectBrowsers().browser_atual)
            if Switch.case('CHROME'):
                driver = webdriver.Chrome(ChromeDriverManager().install())

            if Switch.case('FIREFOX'):
                driver = webdriver.Firefox(GeckoDriverManager().install())
                driver = webdriver.Firefox(executable_path=driver)

            driver.maximize_window()
            return driver
