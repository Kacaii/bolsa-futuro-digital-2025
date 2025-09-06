def main():
    # 18. Contagem de vogais ---------------------------------------------------
    frase = input("Insira uma frase\n > ")
    contador = 0

    for letra in frase:
        match letra:
            case "a" | "e" | "i" | "o" | "u":
                contador += 1
            case _:
                continue

    print(f"Total de vogais: {contador}")


if __name__ == "__main__":
    main()
