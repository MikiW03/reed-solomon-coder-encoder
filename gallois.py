from polynomial import Polynomial


class Gallois:
    m = 6
    t = 12
    irreducible_poly = None
    alpha_powers = None

    def __init__(self):
        self.alpha_powers = self.generate_alpha_powers()

    def poly_2_alpha(self, poly):
        return self.alpha_powers.index(poly)

    def generate_alpha_powers(self):
        alpha = Polynomial([1, 0])
        powers = [Polynomial([1])]
        current = Polynomial([1])

        for i in range(1, 2 ** self.m - 1):
            current *= alpha
            powers.append(current)

        return powers

    def generate_generative_polynomial(self):
        generator_poly = Polynomial([1])

        for i in range(1, 2 * self.t):
            term = self.alpha_powers[0] + self.alpha_powers[i]
            generator_poly *= term

        return generator_poly
