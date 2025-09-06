def main():
    # 6. Dia da Semana ---------------------------------------------------------
    dia_da_semana = int(input("Insira um número (1 a 7)\n > "))

    match dia_da_semana:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda")
        case 3:
            print("Terça")
        case 4:
            print("Quarta")
        case 5:
            print("Quinta")
        case 6:
            print("Sexta")
        case 7:
            print("Sábado")
        case _:
            print("Dia inválido")


if __name__ == "__main__":
    main()
