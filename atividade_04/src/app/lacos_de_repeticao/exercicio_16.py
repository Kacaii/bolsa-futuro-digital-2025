def main():
    # 16. Tabuada Interativa ---------------------------------------------------
    while True:
        numero_escolhido = int(input("Insira um número\n > "))

        for multiplicador in range(1, 11):
            print(
                f"{numero_escolhido} * {multiplicador} = {numero_escolhido * multiplicador}"
            )

        match input("Desenha continuar?\n > "):
            case "sim" | "quero" | "desejo" | "Y":
                continue
            case _:
                break


if __name__ == "__main__":
    main()
