def main():
    # 8. Classificação etária --------------------------------------------------
    idade = int(input("Insira sua idade\n > "))

    if idade >= 0 and idade <= 12:
        print("Criança")
    elif idade >= 13 and idade <= 17:
        print("Adolescente")
    elif idade >= 18 and idade <= 64:
        print("Adulto")
    else:
        print("Idoso")


if __name__ == "__main__":
    main()
