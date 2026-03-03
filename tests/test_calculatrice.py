# tests/test_calculatrice.py
import unittest

from src.calculatrice import division, puissance, moyenne


class TestCalculatrice(unittest.TestCase):

    # -------- division --------
    def test_division_entiers(self):
        self.assertEqual(division(10, 2), 5.0)

    def test_division_decimales(self):
        self.assertEqual(division(5, 2), 2.5)

    def test_division_float_par_float(self):
        self.assertAlmostEqual(division(7.5, 2.5), 3.0)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    # -------- puissance --------
    def test_puissance_classique(self):
        self.assertEqual(puissance(2, 3), 8.0)

    def test_puissance_exposant_zero(self):
        self.assertEqual(puissance(9, 0), 1.0)

    def test_puissance_base_negative(self):
        self.assertEqual(puissance(-2, 3), -8.0)

    def test_puissance_exposant_negatif(self):
        with self.assertRaises(ValueError):
            puissance(2, -1)

    # -------- moyenne --------
    def test_moyenne_plusieurs_valeurs(self):
        self.assertEqual(moyenne([10, 20, 30]), 20.0)

    def test_moyenne_avec_decimales(self):
        self.assertAlmostEqual(moyenne([1.5, 2.5, 3.0]), 7.0 / 3.0)

    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])


if __name__ == "__main__":
    unittest.main()
