def main():
    quantidade_estoque: int = 50
    print(f"Estoque inicial: {quantidade_estoque}")

    valor = int(input("Insira um valor:\n > "))
    quantidade_estoque += valor
    print(f"Estoque final: {quantidade_estoque}")


if __name__ == "__main__":
    main()
