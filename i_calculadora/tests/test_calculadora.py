from i_calculadora.calculadora import Calculadora


def test_calculadora_somar():
    calc = Calculadora()

    inteiro = calc.somar(2, 3)
    assert 5 == inteiro

    decimal = calc.somar(3.33, 6.66)
    assert 9.99 == decimal


def test_calculadora_subtrair():
    calc = Calculadora()

    inteiro = calc.subtrair(3, 2)
    assert 1 == inteiro

    decimal = calc.subtrair(9.99, 6.66)
    assert 3.33 == decimal


def test_calculadora_multiplicar():
    calc = Calculadora()

    inteiro = calc.multiplicar(3, 2)
    assert 6 == inteiro

    decimal = calc.multiplicar(3, 1.11)
    assert 3.33 == decimal


def test_calculadora_dividir():
    calc = Calculadora()

    inteiro = calc.dividir(12, 2)
    assert 6 == inteiro

    decimal = calc.dividir(1.0, 4.0)
    assert 0.25 == decimal

    zero = calc.dividir(9, 0)
    assert 0 == zero
