def main():
    # input --------------------------------------------------------------------
    idade_usuario = int(input("Insira um valor para a sua idade\n > "))
    idade_minima = 18

    # output -------------------------------------------------------------------
    print(f"O usuário é maior de idade? {idade_usuario >= idade_minima}")
    print(f"O usuário é menor de idade? {idade_usuario < idade_minima}")


if __name__ == "__main__":
    main()
