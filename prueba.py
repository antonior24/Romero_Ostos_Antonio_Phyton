import unittest
from calculadora import Calculadora
class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        print("Iniciando pruebas de la calculadora")
        self.calculadoraset = Calculadora(5, 3)
    
    def test_sumar(self):
        print("Prueba de suma correcta")
        calculadora = Calculadora(8,2)
        self.assertNotEqual(calculadora.sumar(), 11)
        self.assertEqual(calculadora.sumar(), 10)
        self.assertEqual(self.calculadoraset.sumar(), 8)
    
    def test_restar(self):
        calculadora = Calculadora(5, 3)
        self.assertEqual(calculadora.restar(), 2)
    
    def test_multiplicar(self):
        calculadora = Calculadora(5, 3)
        self.assertEqual(calculadora.multiplicar(), 15)
    
    def test_dividir(self):
        calculadora = Calculadora(5, 2)
        self.assertEqual(calculadora.dividir(), 2.5)
        calculadora_zero = Calculadora(5, 0)
        with self.assertRaises(ValueError):
            calculadora_zero.dividir()
    
if __name__ == '__main__':
    unittest.main()