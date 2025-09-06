def main():
    # 14. Palíndromo ----------------------------------------------------------
    palavra_escolhida = input("Insira uma palavra\n > ")

    match palavra_escolhida == reversed(palavra_escolhida):
        case True:
            print(f'"{palavra_escolhida}" é um palíndromo')
        case False:
            print(f'"{palavra_escolhida}" não é um palíndromo')


if __name__ == "__main__":
    main()
