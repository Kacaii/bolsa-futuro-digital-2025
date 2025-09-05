def main():
    # input --------------------------------------------------------------------
    numero_tarefas: int = 20
    numero_pessoas: int = int(input("Insira um número\n > "))

    numero_tarefas //= numero_pessoas

    # output -------------------------------------------------------------------
    print(f"Cada tarefa será dividida entre {numero_tarefas} pessoas")


if __name__ == "__main__":
    main()
