import unittest
from polynomial import Polynomial

class TestPolynomial(unittest.TestCase):
    def test_init_trash(self):
        try:
            Polynomial('trash 123')
        except TypeError:
            pass
        except:
            self.fail("Polynomial() raised unexpected exception!")

    def test_init_int(self):
        try:
            Polynomial(1)
        except:
            self.fail("Polynomial() raised unexpected exception!")

    def test_init_float(self):
        try:
            Polynomial(1.0)
        except:
            self.fail("Polynomial() raised unexpected exception!")

    def test_init_list(self):
        try:
            Polynomial([1, 2, 3])
        except:
            self.fail("Polynomial() raised unexpected exception!")

    def test_init_tuple(self):
        try:
            Polynomial((1, 2, 3))
        except:
            self.fail("Polynomial() raised unexpected exception!")

    def test_init_bad_list(self):
        self.assertRaises(ValueError, Polynomial, [1234, "1", "2"])

    def test_add(self):
        p1 = Polynomial((1, 1, 1))
        p2 = Polynomial((2, 2, 2))
        p3 = p1 + p2
        self.assertEqual(Polynomial((3, 3, 3)), p3)

    def test_bad_type_add(self):
        p1 = Polynomial((1, 1, 1))
        self.assertRaises(TypeError, p1.__add__, "abc")

    def test_sub(self):
        p1 = Polynomial((1, 1, 1))
        p2 = Polynomial((2, 2, 2))
        p3 = p2 - p1
        self.assertEqual(Polynomial((1, 1, 1)), p3)

    def test_add_const(self):
        p1 = Polynomial((1, 1))
        p2 = p1 + 1
        self.assertEqual(Polynomial((1, 2)), p2)

    def test_radd_const(self):
        p1 = Polynomial((1, 1))
        p2 = 1 + p1
        self.assertEqual(Polynomial((1, 2)), p2)

    def test_mul_const(self):
        p1 = Polynomial((1, 1))
        p2 = p1 * 2
        self.assertEqual(Polynomial((2, 2)), p2)

    def test_rmul_const(self):
        p1 = Polynomial((1, 1))
        p2 = 2 * p1
        self.assertEqual(Polynomial((2, 2)), p2)

    def test_mul(self):
        p1 = Polynomial((1, 1))
        p1 = Polynomial((2, 1))
        p2 = 2 * p1
        self.assertEqual(Polynomial((4, 2)), p2)

    def test_str(self):
        self.assertEqual(str(Polynomial((1, 2, 3))), 'x^2+2x+3')

    def test_cmp_with_zero_max_pow_coef(self):
        self.assertEqual(Polynomial((1, 2, 3)), Polynomial((0, 1, 2, 3)))

    def test_cmp_with_zero_max_pow_coef(self):
        self.assertEqual(Polynomial((1, 2, 3)), Polynomial((0, 1, 2, 3)))

    def test_cmp_with_zero_max_pow_coef_after_setattr(self):
        a = Polynomial((1, 2, 3))
        b = Polynomial(1)
        b.coefs = [0, 1, 2, 3]
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
