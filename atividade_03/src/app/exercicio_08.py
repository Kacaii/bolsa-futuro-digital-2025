def main():
    # input --------------------------------------------------------------------
    saldo_bancario: int = 1000

    valor_deposito: int = int(input("Insira um valor de depósito\n > "))
    valor_saque: int = int(input("Insira um valor de saque\n > "))
    valor_juros: int = int(input("Insira um valor de juros\n > "))

    saldo_bancario += valor_deposito
    saldo_bancario -= valor_saque
    saldo_bancario *= valor_juros

    # output -------------------------------------------------------------------
    print(f"Valor final: {saldo_bancario}")


if __name__ == "__main__":
    main()
