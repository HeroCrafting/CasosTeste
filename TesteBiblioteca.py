import unittest
from Biblioteca import Biblioteca

'''
- Alisson Santana
- Davy Matos
- Diego Silva
- Laercio Rios
- Luciano Teles
'''

class Testebiblioteca(unittest.TestCase):

    def testCadastrarLivro(self):
        biblioteca = Biblioteca()
        
        self.assertTrue(biblioteca.cadastrarLivro(["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"]))
        self.assertFalse(biblioteca.cadastrarLivro(["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"]))

        self.assertFalse(biblioteca.cadastrarLivro(["978-1-4088-5567-6", "J. K. Rowling"]))

        self.assertFalse(biblioteca.cadastrarLivro(["Harry Potter", "999-9-9999-9999-99", "J. K. Rowling"]))

        self.assertFalse(biblioteca.cadastrarLivro(["Harry Potter", "999-9-9999-9999", "J. K. Rowling"]))

        self.assertFalse(biblioteca.cadastrarLivro(["Harry Potter", "978-1-4088-5567-6"]))

    def testExcluirLivro(self):
        biblioteca = Biblioteca()

        self.assertFalse(biblioteca.deletarLivro("999-9-9999-9999-99"))

        self.assertFalse(biblioteca.deletarLivro("999-9-9999-9999"))

        biblioteca.cadastrarLivro(["A Guerra dos Tronos", "978-8-5441-0292-3", "George R. R. Martin"])
        self.assertTrue(biblioteca.deletarLivro("978-8-5441-0292-3"))

    def testVerificarLivro(self):
        biblioteca = Biblioteca()

        biblioteca.cadastrarLivro(["1984", "978-8-5359-1484-9", "George Orwell"])
        self.assertTrue(biblioteca.buscarLivro("978-8-5359-1484-9"))

        self.assertFalse(biblioteca.buscarLivro("999-9-9999-9999-99"))

        self.assertFalse(biblioteca.buscarLivro("999-9-9999-9999"))

        self.assertFalse(biblioteca.buscarLivro("978-8-5359-1484-8"))
        
    def testListarLivros(self):
        biblioteca = Biblioteca()

        biblioteca.cadastrarLivro(["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"])
        biblioteca.cadastrarLivro(["1984", "978-8-5359-1484-9", "George Orwell"])
        biblioteca.cadastrarLivro(["A Guerra dos Tronos", "978-8-5441-0292-3", "George R. R. Martin"])
        biblioteca.cadastrarLivro(["Medo Clássico", "978-8-5945-4078-2", "H. P. Lovecraft"])
        biblioteca.cadastrarLivro(["Pai rico, pai pobre", "978-8-5508-0148-3", "Robert Kiyosaki"])
        
        livrosCadastrados = biblioteca.listarLivros()

        self.assertEqual(livrosCadastrados[0], ["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"])
        self.assertEqual(livrosCadastrados[1], ["1984", "978-8-5359-1484-9", "George Orwell"])
        self.assertEqual(livrosCadastrados[2], ["A Guerra dos Tronos", "978-8-5441-0292-3", "George R. R. Martin"])
        self.assertEqual(livrosCadastrados[3], ["Medo Clássico", "978-8-5945-4078-2", "H. P. Lovecraft"])
        self.assertEqual(livrosCadastrados[4], ["Pai rico, pai pobre", "978-8-5508-0148-3", "Robert Kiyosaki"])

    def testEmprestarLivro(self):
        biblioteca = Biblioteca()

        biblioteca.cadastrarLivro(["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"])
        self.assertTrue(biblioteca.emprestarLivro("978-1-4088-5567-6"))

        self.assertFalse(biblioteca.emprestarLivro("978-1-4088-5567-6"))

        self.assertFalse(biblioteca.emprestarLivro("978-8-5359-1484-9"))

    def testListarLivrosEmprestados(self):
        biblioteca = Biblioteca()

        biblioteca.cadastrarLivro(["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"])
        biblioteca.emprestarLivro("978-1-4088-5567-6")
        biblioteca.cadastrarLivro(["A Guerra dos Tronos", "978-8-5441-0292-3", "George R. R. Martin"])
        biblioteca.cadastrarLivro(["1984", "978-8-5359-1484-9", "George Orwell"])
        biblioteca.emprestarLivro("978-8-5359-1484-9")

        livrosEmprestados = biblioteca.listarLivrosEmprestados()

        self.assertEqual(livrosEmprestados[0], ["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"])
        self.assertEqual(livrosEmprestados[1], ["1984", "978-8-5359-1484-9", "George Orwell"])

    def testDevolverLivro(self):
        biblioteca = Biblioteca()

        biblioteca.cadastrarLivro(["Harry Potter", "978-1-4088-5567-6", "J. K. Rowling"])
        biblioteca.emprestarLivro("978-1-4088-5567-6")
        self.assertTrue(biblioteca.devolverLivro("978-1-4088-5567-6"))

        self.assertFalse(biblioteca.devolverLivro("978-1-4088-5567-6"))

        self.assertFalse(biblioteca.devolverLivro("978-8-5359-1484-9"))



if __name__ == '__main__':
    unittest.main()
