# Enunciado: Empréstimo Bancário
# Programa Desenvolvido em Python 03 

'''

'''
print()
print('-='*40)
print(f'\033[1;31m{"Testando ":^80}\033[m')
print('-='*40)
print()

from unittest import TestCase, main

from xpto import eh_par


class Testes(TestCase):
    def test_par(self):
        self.assertEqual(eh_par(2), True)

    def test_impar(self):
        self.assertEqual(eh_par(3), False)

    def test_string(self):
        self.assertEqual(eh_par('string'), False)

    def test_float(self):
        self.assertEqual(eh_par(4.5), False)

if __name__ == '__main__':
    main()

   
