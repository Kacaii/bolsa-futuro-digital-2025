def main():
    # 5. Temperatura -----------------------------------------------------------
    temperatura = int(input("Insira a temperatura, em Celsius\n > "))

    if temperatura >= 30:
        print("Muito quente")
    elif temperatura < 15:
        print("Frio")
    else:
        print("Clima agradável")


if __name__ == "__main__":
    main()
