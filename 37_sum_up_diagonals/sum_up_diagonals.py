def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3, 5],
        ...    [4, 5, 6, 6],
        ...    [7, 8, 9, 7],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    first_diagonal = sum(matrix[i][i] for i in range(len(matrix)))
    second_diagonal = sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix)))

    return first_diagonal + second_diagonal

