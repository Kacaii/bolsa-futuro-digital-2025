def main():
    # input --------------------------------------------------------------------
    senha: str = "Python123"
    senha_valida = validar_senha(senha=senha)

    # output -------------------------------------------------------------------
    print(f"A senha é valida? {senha_valida}")


def validar_senha(senha: str) -> bool:
    return (
        (len(senha) != 0)
        and (len(senha) > 8)
        and (senha == "Python123")
        and (senha != "123456")
    )


if __name__ == "__main__":
    main()
