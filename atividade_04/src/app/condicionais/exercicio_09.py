def main():
    # 9. Triângulo -------------------------------------------------------------
    primeiro_lado = int(input("Insira o primeiro lado do triângulo\n > "))
    segundo_lado = int(input("Insira o segundo lado do triângulo\n > "))
    terceiro_lado = int(input("Insira o terceiro lado do triângulo\n > "))

    if primeiro_lado == segundo_lado and segundo_lado == terceiro_lado:
        print("Equilátero")
    elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado:
        print("Isóceles")
    else:
        print("Escaleno")


if __name__ == "__main__":
    main()
