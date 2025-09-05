def main():
    # input --------------------------------------------------------------------
    primeiro_numero: int = int(input("Insira um número:\n > "))
    segundo_numero: int = int(input("Insira outro número:\n > "))

    resultado_potencia = primeiro_numero**segundo_numero
    resultado_divisao_inteira = primeiro_numero // segundo_numero

    # output -------------------------------------------------------------------
    print(f"num1 ** num2 = {resultado_potencia}")
    print(f"num1 // num2 = {resultado_divisao_inteira}")


if __name__ == "__main__":
    main()
