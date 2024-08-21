#Autor: Angie Julieth Ramos Cortes
#CNYT-2. Tarea1. Librería computación Cuántica: Números complejos
#Pruebas Unitext Operaciones de numeros complejos
#21/08/24

import math
import unittest
import libreriaComplejos as lc

class TestComplexNumbers(unittest.TestCase):    

    def test_suma(self):
        self.assertEqual(lc.suma((1, 2), (3, 4)), (4, 6))        #assertEqual: compara la primera parte con la segunda que sean iguales
        self.assertEqual(lc.suma((-1, -2), (1, 2)), (0, 0))

    def test_resta(self):
        self.assertEqual(lc.resta((1, 2), (3, 4)), (-2, -2))
        self.assertEqual(lc.resta((3, 4), (1, 2)), (2, 2))

    def test_producto(self):
        self.assertEqual(lc.producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(lc.producto((0, 1), (1, 0)), (0, 1))

    def test_division(self):
        self.assertEqual(lc.division((1, 2), (3, 4)), (0.44, 0.08))
        self.assertEqual(lc.division((3, 4), (1, 2)), (2.2, -0.4))

    def test_modulo(self):
        self.assertEqual(lc.modulo((3, 4)), 5)
        self.assertEqual(lc.modulo((1, 1)), math.sqrt(2))

    def test_conjugado(self):
        self.assertEqual(lc.conjugado((1, 2)), (1, -2))
        self.assertEqual(lc.conjugado((3, -4)), (3, 4))

    def test_cartesianoAPolar(self):
        self.assertEqual(lc.cartesianoAPolar((1, 1)), (math.sqrt(2), math.pi/4))
        self.assertEqual(lc.cartesianoAPolar((0, 1)), (1, math.pi/2))

    def test_polarACartesiano(self):
        self.assertAlmostEqual(lc.polarACartesiano((1, math.pi/2))[0], 0, places=5)             #assertAlmostEqual ayuda con los errores de punto flotante
        self.assertAlmostEqual(lc.polarACartesiano((1, math.pi/2))[1], 1, places=5)
        self.assertAlmostEqual(lc.polarACartesiano((math.sqrt(2), math.pi/4))[0], 1, places=5)
        self.assertAlmostEqual(lc.polarACartesiano((math.sqrt(2), math.pi/4))[1], 1, places=5)

    def test_fase(self):
        self.assertEqual(lc.fase((1, 1)), math.pi/4)
        self.assertEqual(lc.fase((0, 1)), math.pi/2)

unittest.main()
