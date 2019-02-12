import unittest


class TesteConta(unittest.TestCase):

    def testCadastrar(self):
        self.assertTrue(Conta.cadastararContra(['99999999999', 'José da Silva']))
        self.assertFalse(Conta.cadastararContra(['999999', ' ']))

    def testExculir(self):
        self.assertTrue(Conta.excluirContra(['99999999999', 0.00]))
        self.assertFalse(Conta.excluirConta(' '))
        self.assertFalse(Conta.excluirConta('123'))
        self.assertFalse(Conta.excluirConta(['99999999999', 10.00]))

    def testDepositar(self):
        self.assertTrue(Conta.depositar([5.00]))
        self.assertFalse(Conta.depositar(['0.00']))

    def testSaldo(self):
        self.assertTrue(Conta.alterarLimite(2.00))
        self.assertFalse(Conta.alterarLimite(''))

    def test_transferencia(self):
        self.assertTrue(conta.transferencia((conta.buscarConta("145178-9")), 150))
        self.assertFalse(conta.transferencia((conta.buscarConta("145178-9")), 150))
        self.assertTrue(conta.transferencia((conta.buscarConta("145178-9")), 150))

    def test_saque(self):
        self.assertTrue(conta.saque(100, saldo))
        self.assertFalse(conta.saque(0, saldo))
        self.assertTrue(conta.saque(500, saldo))

    def test_emprestimo(self):
        self.assertTrue(conta.emprestimo(200, conta.credito))
        self.assertFalse(conta.emprestimo(1800, conta.credito))
        self.assertTrue(conta.emprestimo(0, conta.credito))

    def test_consulta_saldo(self):
        self.assertTrue(conta.buscarConta("15478-8"))
        self.assertFalse(conta.buscarConta("0"))

    def test_consulta_limite(self):
        self.assertTrue(conta.buscarConta("15478-4"))
        self.assertFalse(conta.buscarConta("0"))

    def test_conta_no_cpf(self):
        self.assertTrue(conta.consultar_cpf("084.474.965-32"))
        self.assertFalse(conta.consultar_cpf("084.471.855-24"))


if __name__ == '__main__':
    unittest.main()