import random


def main():
    # input --------------------------------------------------------------------
    valor_idade = random.randint(a=0, b=20)
    possui_carteira = True

    pode_dirigir = valor_idade >= 18 and possui_carteira

    # output -------------------------------------------------------------------
    print(f"O usuário pode dirigir? {pode_dirigir}")


if __name__ == "__main__":
    main()
