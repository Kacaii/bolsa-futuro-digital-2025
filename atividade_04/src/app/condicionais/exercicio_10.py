def main():
    # 9. Desconto de compras ---------------------------------------------------
    valor_compra = float(input("Insira o valor total da compra\n > "))
    desconto = 0.0

    if valor_compra >= 500.0:
        desconto = 0.1
    elif valor_compra >= 200.0:
        desconto = 0.05

    print(f"Valor final: ${valor_compra - (valor_compra * desconto)}")


if __name__ == "__main__":
    main()
