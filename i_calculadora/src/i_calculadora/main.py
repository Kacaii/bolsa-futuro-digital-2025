from i_calculadora.calculadora import Calculadora

ascii_calculadora = """┏┓  ┓   ┓   ┓
┃ ┏┓┃┏┓┏┃┏┓┏┫┏┓┏┓┏┓
┗┛┗┻┗┗┗┻┗┗┻┗┻┗┛┛ ┗┻"""
'Uma mensagem em ASCII escrito "Calculadora" '


def main():
    calc = Calculadora()

    #   Loop principal --------------------------------------------------------
    while True:
        print(ascii_calculadora)

        operacao = input("Escolha uma operação matemática\n  > ")

        # Tratamento básico de erros
        try:
            x = float(input(f"Insira o primeiro número para: {operacao}\n  > "))
            y = float(input(f"Insira o segundo número para: {operacao}\n  > "))
        except ValueError:
            print("Número inválido")
            return

        match operacao:
            case "1" | "+" | "soma" | "somar" | "adicionar" | "adicao" | "adição":
                print("Resultado:", calc.somar(x=x, y=y))

            case "2" | "-" | "subtrair" | "subtracao" | "adição":
                print("Resultado:", calc.subtrair(x=x, y=y))

            case "3" | "*" | "x" | "multiplicar" | "multiplicacao" | "multiplicação":
                print("Resultado:", calc.multiplicar(x=x, y=y))

            case "4" | "/" | "dividir" | "divisão":
                print("Resultado:", calc.dividir(x=x, y=y))

            case "":
                return

            case _:
                print("Operação inválida")

    # --------------------------------------------------------------------------


if __name__ == "__main__":
    main()
