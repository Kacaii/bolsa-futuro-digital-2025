def main():
    # input --------------------------------------------------------------------
    numero_dividendo: int = int(input("Insira um número:\n > "))
    numero_divisor: int = int(input("Insira outro número:\n > "))

    resultado_divisao = numero_dividendo / numero_divisor if numero_divisor != 0 else 0
    resultado_resto = numero_dividendo % numero_divisor

    # output -------------------------------------------------------------------
    print(f"divisor / dividendo = {resultado_divisao} | resto = {resultado_resto}")


if __name__ == "__main__":
    main()
