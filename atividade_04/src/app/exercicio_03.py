def main():
    # 3. Senha secreta ---------------------------------------------------------
    senha = int(input("Insira sua senha\n > "))

    match senha == "python123":
        case True:
            print("Acesso permitido")
        case False:
            print("Acesso negado")


if __name__ == "__main__":
    main()
