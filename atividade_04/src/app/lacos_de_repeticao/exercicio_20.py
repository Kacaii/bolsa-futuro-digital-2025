import random


def main():
    # 20. Jogo de adivinhar número ---------------------------------------------
    numero_secreto = random.randint(0, 10)

    while True:
        entrada = int(input(" > "))
        if entrada == numero_secreto:
            break
        elif entrada < numero_secreto:
            print("Insira um número maior")
        elif entrada > numero_secreto:
            print("Insira um número menor")

    print("Acesso autorizado")


if __name__ == "__main__":
    main()
