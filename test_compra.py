from src.page.home_page import HomePage
from src.page.produto_page import ProdutoPage
from src.page.pedido_page import PedidoPage
from src.page.base_page import BasePage
from src.page.authentication.autenticacao_page import AutenticacaoPage
from src.page.authentication.criar_conta_page import CriarContaPage
from src.page.authentication.endereco_entrega_page import EnderecoDeEntregaPage
from src.page.authentication.envio_page import EnvioPage
from src.page.authentication.pagamento_page import PagamentoPage
from src.util.ler_arquivo import LerArquivo
from src.util.data_hora import DataHora
import HtmlTestRunner
import unittest


class TestLoja(unittest.TestCase):

    def setUp(self):
        # diretório de evidências
        self.logs_screen = LerArquivo().parametros().defaults().get('dirlog')
        # data e hora para log
        self.dt_hora = DataHora()
        '''1.Acessar o site: www.automationpractice.com.'''
        self.driver = BasePage().abrir_pagina_base()

    def test_validar_que_quando_realizar_uma_compra_ela_seja_realizada_com_sucesso(self):
        dir_log = self.logs_screen
        nome_cenario = self.id() + '.png'

        '''2.Escolha um produto qualquer na loja.'''
        home = HomePage(self.driver)
        home.clicar_produto_1()
        '''3.Adicione o produto escolhido ao carrinho.'''
        produto = ProdutoPage(self.driver)
        produto.adicionar_produto_ao_pedido()
        '''4.Prossiga para o checkout'''
        produto.ir_checkout()
        '''5.Valide se o produto foi corretamente adicionado ao
            carrinho e prossiga caso esteja tudo certo.'''
        pedido_nome = produto.nome_produto_selecionado()
        pedido = PedidoPage(self.driver)
        self.driver.save_screenshot(dir_log + self.dt_hora.now() + '1' + nome_cenario)
        self.assertTrue(pedido.nome_produto_selecionado(pedido_nome), 'Produto não foi adicionado aos pedidos')
        valor_anuciado = pedido.valor_Total_compra()
        pedido.seguir_com_a_compra()
        '''6.Realize o cadastro do cliente preenchendo todos os
            campos obrigatórios dos formulários.'''
        autenticacao = AutenticacaoPage(self.driver)
        autenticacao.entrar_nova_conta()
        conta = CriarContaPage(self.driver)
        conta.criar_nova_conta()
        '''7.Valide se o endereço está correto e prossiga.'''
        endereco_completo = conta.endereco_completo_do_cadastro()
        endereco_entrega = EnderecoDeEntregaPage(self.driver)
        self.driver.save_screenshot(dir_log + self.dt_hora.now() + '2' + nome_cenario)
        self.assertTrue(endereco_entrega.verificar_endereco_entrega(endereco_completo))
        endereco_entrega.seguir_para_frete()
        '''8.Aceite os termos de serviço e prossiga.'''
        envio = EnvioPage(self.driver)
        envio.aceitar_termos_e_seguir_para_pagamento()
        '''9.Valide o valor total da compra.'''
        pagamento = PagamentoPage(self.driver)
        self.driver.save_screenshot(dir_log + self.dt_hora.now() + '3' + nome_cenario)
        self.assertTrue(pagamento.verificar_valor_total_da_compra_em_pagamento(valor_anuciado))
        '''10.Selecione um método de pagamento e prossiga.'''
        pagamento.pagamento_por_transferencia_bancaria()
        '''11.Confirme a compra e valide se foi finalizada com sucesso.'''
        pagamento.confirmar_pagamento()
        self.driver.save_screenshot(dir_log + self.dt_hora.now() + '4' + nome_cenario)
        self.assertEqual(pagamento.confirmar_pedido_concluido(), 'Your order on My Store is complete.')


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=LerArquivo().parametros_report().defaults().get('dirlog')))
