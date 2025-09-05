def main():
    numero: float = 2.0
    print(f"Valor inicial: {numero}")

    numero_expoente = float(input("Insira um valor:\n > "))
    numero **= numero_expoente
    print(f"Valor final: {numero}")


if __name__ == "__main__":
    main()
