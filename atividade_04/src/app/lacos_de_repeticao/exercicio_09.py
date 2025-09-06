def main():
    # 9. Soma de números informados pelo usuário -------------------------------
    primeiro_numero = int(input("Insira o primeiro valor\n > "))
    segundo_numero = int(input("Insira o segundo valor\n > "))
    terceiro_numero = int(input("Insira o terceiro valor\n > "))
    quarto_numero = int(input("Insira o quarto valor\n > "))
    quinto_numero = int(input("Insira o quinto valor\n > "))

    soma = sum(
        [primeiro_numero, segundo_numero, terceiro_numero, quarto_numero, quinto_numero]
    )

    print(f"Total: {soma}")


if __name__ == "__main__":
    main()
