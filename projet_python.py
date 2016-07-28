'Import to use regex'
import re

class Matrix(object):
    'Common base class for Matrix'

    def _set_number_columns(self, number_columns):
        self._number_columns = number_columns

    def _get_number_columns(self):
        return self._number_columns

    def _set_number_rows(self, number_rows):
        self._number_rows = number_rows

    def _get_number_rows(self):
        return self._number_rows

    def _set_matrix(self, matrix):
        self._matrix = matrix

    def _get_matrix(self):
        return self._matrix

    def fill_matrix(self):
        'Methods to fill a matrix'
        for i in range(self._number_columns):
            values = input("Entrer "+str(self._number_rows)+" nombre séparé par des virgules: ")
            self._matrix[i] = values.split(",")

    def _sum_matrix(self, _mat):
        if _mat is not None:
            if isinstance(_mat, Matrix):
                # Each matrix MUST be the same dimension
                if self._number_columns == _mat._number_columns\
                and self._number_rows == _mat._number_rows:
                    result = Matrix(self._number_columns, _mat._number_rows)
                    for i in range(self._number_rows):
                        for j in range(self._number_columns):
                            result._matrix[i][j] = int(self._matrix[i][j]) + int(_mat._matrix[i][j])
                    return result
        return None

    def _substract_matrix(self, _mat):
        if _mat is not None:
            if isinstance(_mat, Matrix):
                # Each matrix MUST be the same dimension
                if self._number_columns == _mat._number_columns\
                and self._number_rows == _mat._number_rows:
                    result = Matrix(self._number_columns, _mat._number_rows)
                    for i in range(self._number_rows):
                        for j in range(self._number_columns):
                            result._matrix[i][j] = int(self._matrix[i][j]) - int(_mat._matrix[i][j])
                    return result
        return None

    def _multiply_matrix(self, _mat):
        'Method to multiply matrixes'
        if _mat is not None:
            if isinstance(_mat, Matrix):
                # The number of columns of a matrix A MUST be
                # equals to the number of rows of the matrix B
                if self._number_columns == _mat._number_rows:
                    result = Matrix(self._number_columns, _mat._number_rows)
                    row = []
                    for i in range(self._number_columns):
                        for j in range(_mat._number_rows):
                            total = 0
                            for k in range(self._number_rows):
                                total += int(self._matrix[i][k]) * int(_mat._matrix[k][j])
                            row.append(total)
                        result._matrix[i] = row
                        row = []
                    return result
        return None

    def _save_matrix(self, filename):
        file = open(filename+'.matrix', 'w+')
        text = "[" + str(self._number_columns) + "][" + str(self._number_rows) + "]={"
        for i in range(self._number_columns):
            text = text + "["
            for j in range(self._number_rows):
                text = text + str(self._matrix[i][j])+","
            text = text[:-1]
            text = text + "]"
        text = text + "}"
        file.write(text)

    def _load_matrix(self, filename):
        file = open(filename+'.matrix')
        for line in file:
            row_pattern = r"(\[((-*\d+,)*-*\d+)\])"
            row_string = re.compile(r''+row_pattern).findall(line)
            count_row = 0
            invalide_number_rows = 0
            row_content = []
            number_rows_of_file = int(row_string[0][1])
            number_columns_of_file = int(row_string[1][1])
            for i in range(2, len(row_string)):
                row_content = row_string[i][1].split(',')
                j = 0
                for value in row_content:
                    self._matrix[i-2][j] = value
                    j += 1
                if len(row_content) != number_columns_of_file:
                    invalide_number_rows = 1
                    break
                count_row += 1
            if count_row == number_rows_of_file and invalide_number_rows == 0\
            and number_columns_of_file == self._number_columns and\
            number_rows_of_file == self._number_rows:
                if re.compile(r'\[(\d)]\[(\d)]={'+row_pattern+'*}').match(line):
                    print("Le fichier est valide")
                else:
                    print("Le fichier est invalide")

    def display(self):
        'Method to display a matrix'
        max_length_per_column = []
        for index_long in range(self._number_rows):
            max_length_per_column.append(self._longest_of_the_column(index_long))
        for i in range(self._number_columns):
            row_content = ""
            for j in range(self._number_rows):
                row_content += str(self._matrix[i][j])
                k = 0
                for space in range(max_length_per_column[j] - len(str(self._matrix[i][j])) + 1):
                    row_content += " "
            print(row_content)

    def _longest_of_the_column(self, row_index):
        longest = 0
        if row_index >= self._number_rows:
            return -1
        for i in range(self._number_columns):
            if len(str(self._matrix[i][row_index])) > longest:
                longest = len(str(self._matrix[i][row_index]))
        return longest

    def __init__(self, number_columns, number_rows):
        self._number_columns = number_columns
        self._number_rows = number_rows
        self._matrix = [[0 for x in range(number_rows)] for y in range(number_columns)]
