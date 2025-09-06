def main():
    # 1. Par ou Ímpar ----------------------------------------------------------
    numero = int(input("Insira um número\n > "))

    match numero % 2:
        case 0:
            print("Par")
        case _:
            print("Ímpar")


if __name__ == "__main__":
    main()
