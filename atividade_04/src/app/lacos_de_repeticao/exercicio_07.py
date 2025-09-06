def main():
    # 6. Tabuada personalizada ---------------------------------------------------
    numero_escolhido = int(input("Insira um número\n > "))
    for numero in range(1, 11):
        print(f"{numero_escolhido} * {numero} = {(numero_escolhido * numero)}")


if __name__ == "__main__":
    main()
