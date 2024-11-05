from gallois import Gallois
from polynomial import Polynomial

import unittest


class TestOperations(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestOperations, self).__init__(*args, **kwargs)
        Polynomial.irreducible_poly = Polynomial([1, 0, 0, 0, 0, 1, 1])

    def test_addition(self):
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
        p1 = Polynomial([1, 0, 0, 0, 0, 1])
        p2 = Polynomial([1, 1, 0, 1, 0, 1])
        self.assertEqual(p1/p2, Polynomial([1, 0, 1, 1, 1, 1]))

        p3 = Polynomial([1, 1])
        p4 = Polynomial([1, 1, 0, 1])
        self.assertEqual(p3 / p4, Polynomial([1, 1, 1, 0, 1, 1]))

        p5 = Polynomial([1, 1, 1, 1, 1, 1])
        p6 = Polynomial([0])
        self.assertEqual(p5 / p6, None)
        self.assertEqual(p6 / p5, Polynomial([0]))

        p7 = Polynomial([1])
        self.assertEqual(p5 / p7, p5)

    def test_multiplication(self):
        p1 = Polynomial([1, 1, 0, 1])
        p2 = Polynomial([1, 0, 1, 1])
        self.assertEqual(p1 * p2, Polynomial([1, 1, 1, 1, 0, 0]))

        p3 = Polynomial([1, 0, 1, 0, 1, 1])
        p4 = Polynomial([1, 1, 0, 1, 1, 0])
        self.assertEqual(p3 * p4, Polynomial([1, 1, 1, 0]))

        p5 = Polynomial([1, 0, 1, 1])
        p6 = Polynomial([1, 1, 0])
        self.assertEqual(p5 * p6, Polynomial([1, 1, 1, 0, 1, 0]))

    def test_inverse(self):
        p1 = Polynomial([1, 1])
        self.assertEqual(p1.get_inverse(), Polynomial([1, 1, 1, 1, 1, 0]))

        p2 = Polynomial([1, 1, 1, 1, 1, 1])
        self.assertEqual(p2.get_inverse(), Polynomial([1, 0, 0, 0, 0, 0]))

        p3 = Polynomial([1, 0, 0, 1, 0, 1])
        self.assertEqual(p3.get_inverse(), Polynomial([1, 0, 0, 1]))

        p4 = Polynomial([1, 1, 0, 1, 0, 1])
        self.assertEqual(p4.get_inverse(), Polynomial([1, 1, 1, 0, 1]))


if __name__ == '__main__':
    unittest.main()
