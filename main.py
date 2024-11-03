from gallois import Gallois
from output import Output
from polynomial import Polynomial


if __name__ == '__main__':
    M = 6
    T = 12
    IRREDUCIBLE_POLY = Polynomial([1, 0, 0, 0, 0, 1, 1])

    Gallois.m = Polynomial.m = M
    Gallois.t = Polynomial.t = T
    Gallois.irreducible_poly = Polynomial.irreducible_poly = IRREDUCIBLE_POLY

    gallois = Gallois()
    output = Output()

    # alpha_powers_filled = list(map(lambda x: x.get_filled(6), gallois.alpha_powers))
    # output.generate_alpha_powers_file(alpha_powers_filled)
    # output.generate_addition_table_file(alpha_powers_filled)
    # output.generate_multiplication_table_file(alpha_powers_filled)
