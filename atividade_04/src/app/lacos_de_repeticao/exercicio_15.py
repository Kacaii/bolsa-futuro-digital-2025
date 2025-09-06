def main():
    # 15. Senha até acertar ----------------------------------------------------
    senha = "python123"

    while True:
        if input("Insira uma palavra\n > ") == senha:
            break

    print("Acesso autorizado")


if __name__ == "__main__":
    main()
