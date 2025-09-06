def main():
    # 10. Média de notas -------------------------------------------------------
    primeira_nota = int(input("Insira a primeira nota\n > "))
    segunda_nota = int(input("Insira a segunda nota\n > "))
    terceira_nota = int(input("Insira a terceira nota\n > "))

    notas = [primeira_nota, segunda_nota, terceira_nota]
    media_final = sum(notas) / len(notas)

    print(f"Média final: {media_final}")


if __name__ == "__main__":
    main()
