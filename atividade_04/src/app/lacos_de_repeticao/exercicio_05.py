def main():
    # 5. Mostrar números ímpares de 0 a 50 ---------------------------------------
    numero_pares = filter(lambda x: x % 2 != 0, range(0, 51))
    for numero in numero_pares:
        print(f"{numero}", end=" ")


if __name__ == "__main__":
    main()
