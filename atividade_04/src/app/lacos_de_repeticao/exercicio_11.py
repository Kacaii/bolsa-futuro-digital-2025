def main():
    # 11. Número positivo ou negativo ------------------------------------------
    primeiro_numero = int(input("Insira o primeiro valor\n > "))
    segundo_numero = int(input("Insira o segundo valor\n > "))
    terceiro_numero = int(input("Insira o terceiro valor\n > "))
    quarto_numero = int(input("Insira o quarto valor\n > "))
    quinto_numero = int(input("Insira o quinto valor\n > "))

    numeros = [
        primeiro_numero,
        segundo_numero,
        terceiro_numero,
        quarto_numero,
        quinto_numero,
    ]

    for numero in numeros:
        match numero >= 0:
            case True:
                print("Positivo", end=" ")
            case False:
                print("Negativo", end=" ")

    print("Feito!")


if __name__ == "__main__":
    main()
