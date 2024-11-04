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

    def binary_vector_division(self, dividend, divisor):
        # Ensure the dividend is at least as long as the divisor
        len_dividend = len(dividend)
        len_divisor = len(divisor)

        # Initialize quotient and remainder
        quotient = [0] * (len_dividend - len_divisor + 1)
        remainder = dividend.copy()

        for i in range(len_dividend - len_divisor + 1):
            # Check if the current leading term of the remainder can be divided
            if remainder[i] == 1:  # This means we can divide
                # Set the corresponding position in the quotient to 1
                quotient[i] = 1
                # Perform XOR with the shifted divisor
                for j in range(len_divisor):
                    remainder[i + j] ^= divisor[j]

        # The remainder now holds the result of the division
        # Remove leading zeros from the remainder
        while len(remainder) > 0 and remainder[0] == 0:
            remainder.pop(0)

        return quotient, remainder

    def to_string(self):
        poly = self.coefficients
        if len(poly) == 0:
            return "0"

        terms = []
        degree = len(poly) - 1

        for i in range(degree, -1, -1):
            if poly[degree - i] == 1:
                if i == 0:
                    terms.append("1")
                elif i == 1:
                    terms.append("x")
                else:
                    terms.append(f"x^{i}")

        return " + ".join(terms)

    def get_inverse(self):
        dividend = self.irreducible_poly.coefficients
        divisor = self.coefficients

        if divisor == [0]:
            return None
        elif divisor == [1]:
            return Polynomial([1])

        matter = []

        quotient, remainder = self.binary_vector_division(dividend, divisor)
        matter.append(((6 - len(quotient)) * [0]) + quotient)

        remainders = [remainder]

        while remainder != [1]:
            dividend = divisor
            divisor = remainder
            quotient, remainder = self.binary_vector_division(dividend, divisor)
            matter.append(((6 - len(quotient)) * [0]) + quotient)
            remainders.append(remainder)

        if len(remainders) > 1:
            matter.append(((6 - len(remainders[-2])) * [0]) + remainders[-2])

        zerob = [0, 0, 0, 0, 0, 0]
        oneb = [0, 0, 0, 0, 0, 1]

        final_val = Polynomial(zerob)

        if len(matter) == 1:
            final_val += Polynomial(matter[0])

            return final_val
        elif len(matter) == 3:
            final_val += Polynomial(matter[0])
            final_val *= Polynomial(matter[1])
            final_val += Polynomial(oneb)

            return final_val
        elif len(matter) > 3:
            prog_values = []
            final_val += Polynomial(matter[0])
            prog_values.append(final_val)
            final_val *= Polynomial(matter[1])
            final_val += Polynomial(oneb)
            prog_values.append(final_val)

            for you in matter[2:len(matter) - 1]:
                final_val = prog_values[1] * Polynomial(you)
                prog_values[0] += final_val
                prog_values[1], prog_values[0] = prog_values[0], prog_values[1]

            return prog_values[1]

    def __truediv__(self, other):
        return None if self is None or other.get_inverse() is None else self * other.get_inverse()

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))

        coefficients1 = self.get_filled(max_len).coefficients
        coefficients2 = other.get_filled(max_len).coefficients

        result = [(coefficients1[i] if i < len(coefficients1) else 0) ^
                  (coefficients2[i] if i < len(coefficients2) else 0)
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
            if a & 2 ** self.m:
                a ^= self.irreducible_poly.get_value()
            b >>= 1

        return Polynomial([int(x) for x in bin(result)[2:]])
