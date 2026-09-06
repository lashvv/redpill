from redpill.matrix import Matrix
import pytest

def test_validation():
    with pytest.raises(ValueError, match="All rows must have the same number of columns."):
        Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8]
        ])

def test_empty():
    with pytest.raises(ValueError, match="Matrix cannot be empty."):
        Matrix([])



def test_addition():
    A = Matrix([
        [1, 2],
        [3, 4]
    ])

    B = Matrix([
        [5, 6],
        [7, 8]
    ])

    result = A + B

    assert result == Matrix([
        [6, 8],
        [10, 12]
    ])

def test_mul():
    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    scalar = 5

    result = A * scalar

    assert result == Matrix([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ])

def test_rmul():
    A = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])

    scalar = 5

    result = scalar * A

    assert result == Matrix([
        [5, 10, 15],
        [20, 25, 30],
        [35, 40, 45]
    ])