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
        elif type(coefs) in (int, float):
            self.coefs = [coefs]
        else:
            raise TypeError("coefs should be list, tuple, Polynomial or single int, float")

    @staticmethod
    def __coef_to_term(number):
        if number > 0:
            return f'+{number}'
        elif number < 0:
            return str(number)
        else:
            return None

    @staticmethod
    def __get_sign(number):
        if number > 0:
            return f''
        elif number < 0:
            return f'-'
        else:
            return None

    def __str__(self):
        pol_as_str = ''
        is_first_coef = True
        if self.max_pow == 0:
            return str(self.coefs[0])
        else:
            curr_pow = self.max_pow
            for coef in self.coefs:
                if coef != 0:
                    if not is_first_coef:
                        if coef == -1 and curr_pow != 0:
                            pol_as_str += '-'
                        elif coef == 1 and curr_pow != 0:
                            pol_as_str += '+'
                        else:
                            pol_as_str += self.__coef_to_term(coef)
                    else:
                        pol_as_str = str(self.__get_sign(coef)) if coef == 1 or coef == -1 \
                                                                else str(coef)
                        is_first_coef = False
                    if curr_pow == 1:
                        pol_as_str += f'x'
                    elif curr_pow != 0:
                        pol_as_str += f'x^{curr_pow}'
                curr_pow -= 1
        return pol_as_str

    def __repr__(self):
        return f"Polynomial({self.coefs})"

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if key == "coefs":
            self.max_pow = len(self.coefs) - 1

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
        if type(other) == Polynomial:
            coefs = other.coefs.copy()
        elif type(other) in (float, int):
            coefs = [other]
        else:
            raise TypeError(f"can't sub {type(self)} with {type(other)}")
        for i in range(0, len(coefs)):
            coefs[i] = -coefs[i]
        return self.__add__(Polynomial(coefs))

    def __rsub__(self, other):
        tmp = Polynomial(self)
        for i in range(0, len(tmp.coefs)):
            tmp.coefs[i] = -tmp.coefs[i]
        return tmp.__add__(other)

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
            else:
                return False
        elif type(other) is Polynomial:
            return self.coefs == other.coefs
        else:
            raise TypeError(f"can't compare {type(self)} with {type(other)}")

    __radd__ = __add__
    __rmul__ = __mul__ 
