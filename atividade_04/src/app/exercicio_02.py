def main():
    # 2. Maioridade ------------------------------------------------------------
    idade = int(input("Insira a sua idade\n > "))

    match idade >= 18:
        case True:
            print("Maior de idade")
        case False:
            print("Menor de idade")


if __name__ == "__main__":
    main()
