class Calculadora:
    """  Calculadora para operações matemáticas básicas"""

    def somar(self, x: float, y: float) -> float:
        """  Retorna o resultado da soma de `x` e `y`"""
        return x + y

    def subtrair(self, x: float, y: float) -> float:
        """  Retorna o resultado da subtração de `x` e `y`"""
        return x - y

    def multiplicar(self, x: float, y: float) -> float:
        """  Retorna o resultado da multiplicação de `x` por `y`"""
        return x * y

    def dividir(self, x: float, y: float) -> float:
        """
          Retorna o resultado da divisão de `x` por `y`
        Ao invés de gerar um erro, divisão por zero retorna zero
        """
        return 0 if y == 0 or y == 0.0 else x / y
