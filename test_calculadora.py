from calculadora import multiplicacion, resta, suma


def test_suma():
    assert suma(2, 3) == 5


def test_resta():
    assert resta(5, 2) == 3


def test_multiplicacion():
    assert multiplicacion(3, 3) == 9