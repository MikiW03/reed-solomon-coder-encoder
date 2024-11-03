class Polynomial:
    m = 6
    t = 12
    irreducible_poly = None

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __repr__(self):
        return f"{self.coefficients}"

    def __eq__(self, other):
        return str(self.get_trimmed()) == str(other.get_trimmed())

    def get_value(self):
        num = 0
        for (index, b) in enumerate(reversed(self.coefficients)):
            num += b * (2 ** index)
        return num

    def get_degree(self):
        return len(self.coefficients) - 1

    def get_trimmed(self):
        coefficients_copy = self.coefficients[:]
        while len(coefficients_copy) > 1 and coefficients_copy[0] == 0:
            coefficients_copy.pop(0)
        return Polynomial(coefficients_copy)

    def get_filled(self, desired_no_of_bits):
        coefficients_copy = self.coefficients[:]
        for _ in range(desired_no_of_bits - len(self.coefficients)):
            coefficients_copy = [0] + coefficients_copy
        return Polynomial(coefficients_copy)

    def get_inverse(self):
        # TODO odwrotność w mnożeniu
        return

    def __truediv__(self, other):
        # TODO dzielenie
        return self * Polynomial(other.get_multiplicative_inverse())

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [(self.coefficients[i] if i < len(self.coefficients) else 0) ^
                  (other.coefficients[i] if i < len(other.coefficients) else 0)
                  for i in range(max_len)]
        return Polynomial(result)

    def __mul__(self, other):
        result = 0
        a = self.get_value()
        b = other.get_value()
        while b > 0:
            if b & 1:
                result ^= a
            a <<= 1
            if a & 2**self.m:
                a ^= self.irreducible_poly.get_value()
            b >>= 1

        return Polynomial([int(x) for x in bin(result)[2:]])
