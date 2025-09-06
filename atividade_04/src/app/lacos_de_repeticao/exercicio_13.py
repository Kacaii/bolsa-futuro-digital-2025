def main():
    # 13. Contar letras de uma palavra -----------------------------------------
    palavra_escolhida = input("Insira uma palavra\n > ")

    contador = 0
    for _ in palavra_escolhida:
        contador += 1

    print(f'"{palavra_escolhida}" tem um total de {contador} letras')


if __name__ == "__main__":
    main()
