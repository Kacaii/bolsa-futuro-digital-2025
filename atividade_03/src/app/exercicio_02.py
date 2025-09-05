def main():
    # input --------------------------------------------------------------------
    primeiro_numero: float = float(input("Insira um número:\n > "))
    segundo_numero: float = float(input("Insira outro número:\n > "))

    resultado_multiplicacao = primeiro_numero + segundo_numero
    resultado_divisao = primeiro_numero - segundo_numero

    # output -------------------------------------------------------------------
    print(f"num1 * num2 = {resultado_multiplicacao}")
    print(f"num1 / num2 = {resultado_divisao}")


if __name__ == "__main__":
    main()
