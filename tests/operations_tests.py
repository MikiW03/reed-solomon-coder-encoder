from gallois import Gallois
from polynomial import Polynomial

import unittest


class TestOperations(unittest.TestCase):
    def test_addition(self):
        Polynomial.irreducible_poly = Polynomial([1, 0, 0, 0, 0, 1, 1])

        p1 = Polynomial([1, 0])
        p2 = Polynomial([0, 1])
        self.assertEqual(p1 + p2, Polynomial([1, 1]))

        p3 = Polynomial([1, 0, 1, 0, 1, 1])
        p4 = Polynomial([1, 1, 0, 1, 1, 0])
        self.assertEqual(p3 + p4, Polynomial([0, 1, 1, 1, 0, 1]))

        p5 = Polynomial([1, 0, 1, 0])
        p6 = Polynomial([1, 0, 1])
        self.assertEqual(p5 + p6, Polynomial([1, 1, 1, 1]))

        p7 = Polynomial([1, 0])
        p8 = Polynomial([1, 0, 0])
        self.assertEqual(p7 + p8, Polynomial([1, 1, 0]))

    def test_division(self):
        Polynomial.irreducible_poly = Polynomial([1, 0, 0, 0, 0, 1, 1])
        pass

    def test_multiplication(self):
        Polynomial.irreducible_poly = Polynomial([1, 0, 0, 0, 0, 1, 1])

        p1 = Polynomial([1, 1, 0, 1])
        p2 = Polynomial([1, 0, 1, 1])
        self.assertEqual(p1 * p2, Polynomial([1, 1, 1, 1, 0, 0]))

        p3 = Polynomial([1, 0, 1, 0, 1, 1])
        p4 = Polynomial([1, 1, 0, 1, 1, 0])
        self.assertEqual(p3 * p4, Polynomial([1, 1, 1, 0]))

    def test_inverse(self):
        Polynomial.irreducible_poly = Polynomial([1, 0, 0, 0, 0, 1, 1])

        p1 = Polynomial([1, 1])
        self.assertEqual(p1.get_inverse(), Polynomial([1, 1, 1, 1, 1, 0]))


if __name__ == '__main__':
    M = 6
    T = 12
    IRREDUCIBLE_POLY = Polynomial([1, 0, 0, 0, 0, 1, 1])

    Gallois.m = Polynomial.m = M
    Gallois.t = Polynomial.t = T
    Gallois.irreducible_poly = Polynomial.irreducible_poly = IRREDUCIBLE_POLY

    gallois = Gallois()
    unittest.main()
