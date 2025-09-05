def main():
    # input --------------------------------------------------------------------
    primeiro_numero: float = float(input("Insira um número:\n > "))
    segundo_numero: float = float(input("Insira outro número:\n > "))

    resultado_soma = primeiro_numero + segundo_numero
    resultado_subtracao = primeiro_numero - segundo_numero

    # output -------------------------------------------------------------------
    print(f"num1 + num2 = {resultado_soma}")
    print(f"num1 + num2 = {resultado_subtracao}")


if __name__ == "__main__":
    main()
