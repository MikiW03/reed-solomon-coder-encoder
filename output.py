import pandas
import numpy


class Output:
    @staticmethod
    def generate_addition_table_file(tab):
        addition_table = numpy.add.outer(tab, tab)
        df = pandas.DataFrame(addition_table)
        df.columns = df.index = tab
        df.to_excel("output_files\\addition_table.xlsx")

    @staticmethod
    def generate_multiplication_table_file(tab):
        multiplication_table = numpy.multiply.outer(tab, tab)
        df = pandas.DataFrame(multiplication_table)
        df.columns = df.index = tab
        df.to_excel("output_files\\multiplication_table.xlsx")

    @staticmethod
    def generate_alpha_powers_file(tab):
        alpha_powers_np = numpy.array(tab)
        df = pandas.DataFrame(alpha_powers_np)
        df.index = [f"alpha^{x}" for x in range(0, 63)]
        df.columns = ["binary_representation"]
        df.to_excel("output_files\\alpha_powers.xlsx")
