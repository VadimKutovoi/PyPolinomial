#!/bin/env python3

class Polynomial:
    def __init__(self, coefs):
        if not coefs:
            raise ValueError("coefs is empty!")
        if type(coefs) in (list, tuple):
            for coef in coefs:
                if type(coef) not in (int, float):
                    raise ValueError("coefs list should contain only int or float")
            self.coefs = list(coefs)
            self.max_pow = len(coefs) - 1
        elif type(coefs) is Polynomial:
            self.coefs = coefs.coefs.copy()
            self.max_pow = coefs.max_pow
        else:
            raise TypeError("coefs should be list or Polynomial")

    def __str__(self):
        pol_as_str = ''
        curr_pow = self.max_pow
        if self.max_pow > 0:
            for coef in self.coefs[0:self.max_pow - 1]:
                if not coef == 0:
                    pol_as_str += str(coef) + f'x^{curr_pow} + '
                curr_pow -= 1
            if (self.coefs[-2] != 0):
                pol_as_str += str(self.coefs[-2]) + f'x + '
            if (self.coefs[-1] != 0):
                pol_as_str += str(self.coefs[-1])
        return pol_as_str

    def __repr__(self):
        return f"Polynomial({self.coefs})"

    def __add__(self, other):
        if type(other) in (int, float):
            coefs = self.coefs.copy()
            coefs[-1] += other
        elif type(other) is Polynomial:
            i = -1
            if other.max_pow >= self.max_pow:
                coefs = other.coefs.copy()
                while i > -(self.max_pow + 2):
                    coefs[i] += self.coefs[i]
                    i -= 1
            else:
                coefs = self.coefs.copy()
                while i > -(other.max_pow + 2):
                    coefs[i] += other.coefs[i]
                    i -= 1
        else:
            raise TypeError(f"can't add {type(self)} with {type(other)}")
        return Polynomial(coefs)

    def __sub__(self, other):
        coefs = other.coefs.copy()
        for i in range(0, len(coefs)):
            coefs[i] = -coefs[i]
        return self.__add__(Polynomial(coefs))

    def __mul__(self, other):
        if type(other) in (int, float):
            coefs = self.coefs.copy()
            for i in range(self.max_pow + 1):
                coefs[i] *= other
        elif type(other) is Polynomial:
            coefs = [0] * (self.max_pow + other.max_pow + 1)
            for i in range(self.max_pow + 1):
                for j in range(other.max_pow + 1):
                    coefs[i + j] += self.coefs[i] * other.coefs[j]
        else:
            raise TypeError(f"can't multiply {type(self)} with {type(other)}")
        return Polynomial(coefs)

    def __eq__(self, other):
        if type(other) in (int, float):
            if self.max_pow == 0:
                return self.coefs[-1] == other
        elif type(other) is Polynomial:
            return self.coefs == other.coefs
        else:
            raise TypeError(f"can't compare {type(self)} with {type(other)}")

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__ 
