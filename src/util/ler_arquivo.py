
import configparser
import os.path

class LerArquivo():

    diretorio_paremetros = '.\\src\\resources\\config'
    nome_arquivo = 'dir_print'

    def parametros(self):
        self._nome_arquivo = '\\' + self.nome_arquivo + '.cfg'
        self._arquivo = self.diretorio_paremetros + self._nome_arquivo
        root_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
        path = os.path.join(os.path.split(root_path)[0], self._arquivo)
        config = configparser.ConfigParser()
        config.read(path)
        return config

if __name__ == '__main__':
    aa = LerArquivo()
    bb = aa.parametros()
    print(bb.defaults().get('dirlog'))
