import unittest
from polynomial import Polynomial


class TestPolynomial(unittest.TestCase):
    a = Polynomial([1, 1, 1])
    b = Polynomial([2, 2, 2])
    const = 100

    def test_init_empty(self):
        with self.assertRaises(TypeError):
            Polynomial()

    def test_init_empty_list_raise_TypeError(self):
        with self.assertRaises(ValueError):
            a = Polynomial([])

    def test_init_invalid_args(self):
        with self.assertRaises(TypeError):
            Polynomial("asdkhjkklj123")

    def test_init_const(self):
        self.assertEqual(Polynomial(10), 10)

    def test_init_tuple(self):
        self.assertEqual(str(Polynomial((1, 2, 3))), "x^2+2x+3")

    def test_init_list(self):
        self.assertEqual(str(Polynomial([1, 2, 3])), "x^2+2x+3")

    def test_add_polynomial(self):
        self.assertEqual(self.a + self.b, Polynomial([3, 3, 3]))

    def test_mul_polynomial(self):
        self.assertEqual(self.a * self.b, Polynomial([2, 4, 6, 4, 2]))

    def test_sub_polynomial(self):
        self.assertEqual(self.a - self.b, Polynomial([-1, -1, -1]))

    def test_add_right_const(self):
        self.assertEqual(self.a + self.const, Polynomial([1, 1, 101]))

    def test_add_left_const(self):
        self.assertEqual(self.const + self.a, Polynomial([1, 1, 101]))

    def test_mul_right_const(self):
        self.assertEqual(self.a * self.const, Polynomial([100, 100, 100]))

    def test_mul_left_const(self):
        self.assertEqual(self.const * self.a, Polynomial([100, 100, 100]))

    def test_sub_right_const(self):
        self.assertEqual(self.a - self.const, Polynomial([1, 1, -99]))

    def test_sub_left_const(self):
        self.assertEqual(self.const - self.a, Polynomial([-1, -1, 99]))

    def test_add_raise_TypeError(self):
        with self.assertRaises(TypeError):
            self.a + "my_string"

    def test_mul_raise(self):
        with self.assertRaises(TypeError):
            self.b * "my_string"

    def test_sub_raise(self):
        with self.assertRaises(TypeError):
            self.b - "my_string"

    def test_eq_polynom_False(self):
        self.assertEqual(self.a == self.b, False)

    def test_eq_polynom_True(self):
        self.assertEqual(self.a == Polynomial((1, 1, 1)), True)

    def test_eq_const_False(self):
        self.assertEqual(self.a == 10, False)

    def test_eq_const_True(self):
        self.assertEqual(Polynomial(100) == 100, True)

    def test_repr(self):
        self.assertEqual(repr(self.a), "Polynomial([1, 1, 1])")
