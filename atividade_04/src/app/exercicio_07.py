def main():
    # 7. Maior de três números -------------------------------------------------
    primeiro_numero = int(input("Insira o primeiro número\n > "))
    segundo_numero = int(input("Insira o segundo número\n > "))
    terceiro_numero = int(input("Insira o terceiro número\n > "))

    maior_número = max([primeiro_numero, segundo_numero, terceiro_numero])
    print(f"Maior número: {maior_número}")


if __name__ == "__main__":
    main()
