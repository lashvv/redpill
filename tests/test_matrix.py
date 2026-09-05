from redpill.matrix import Matrix


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