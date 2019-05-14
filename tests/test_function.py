from function import factorial


def test_givenzero_factorial_retunszero():
    assert factorial(0) == 1


def test_givenone_factorial_retunsone():
    assert factorial(1) == 1
