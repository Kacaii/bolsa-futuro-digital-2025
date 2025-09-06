def main():
    # 17. Soma de pares --------------------------------------------------------
    numeros: list[int] = []
    for _ in range(10):
        valor = int(input("Insira um valor\n > "))
        numeros.append(valor)

    numeros_pares = filter(lambda x: x % 2 == 0, numeros)
    print(f"Soma dos pares: {sum(numeros_pares)}")


if __name__ == "__main__":
    main()
