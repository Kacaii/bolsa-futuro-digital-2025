def main():
    # 4. Nota escolar ----------------------------------------------------------
    nota = int(input("Insira sua nota\n > "))

    if nota >= 9:
        print("Excelente!")
    elif nota >= 7:
        print("Bom")
    elif nota < 7:
        print("Precisa melhorar")


if __name__ == "__main__":
    main()
