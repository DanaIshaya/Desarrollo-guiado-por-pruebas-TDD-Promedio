import unittest

# Función para calcular el promedio de un arreglo de números enteros
def calcular_promedio(conjunto):
    if len(conjunto) == 0:
        return 0.0
    return sum(conjunto) / len(conjunto)

# Clase de pruebas unitarias para la función calcular_promedio
class TestCalcularPromedio(unittest.TestCase):
    def test_positivos(self):
        self.assertEqual(calcular_promedio([1, 2, 3, 4, 5]), 3.0)
    
    def test_negativos(self):
        self.assertEqual(calcular_promedio([-1, -2, -3, -4, -5]), -3.0)
    
    def test_mixtos(self):
        self.assertEqual(calcular_promedio([-1, 1, -2, 2, -3, 3]), 0.0)
    
    def test_un_solo_numero(self):
        self.assertEqual(calcular_promedio([42]), 42.0)
    
    def test_repetidos(self):
        self.assertEqual(calcular_promedio([5, 5, 5, 5, 5]), 5.0)
    
    def test_vacio(self):
        self.assertEqual(calcular_promedio([]), 0.0)

if __name__ == '__main__':
    unittest.main()
