from .animal import Animal


def main():
    # 1. -----------------------------------------------------------------------
    animais: list[Animal] = [
        Animal(nome="Leonardo", especie="Tartaruga", vertebrado=True),
        Animal(nome="Rafael", especie="Tartaruga", vertebrado=True),
        Animal(nome="Donatello", especie="Tartaruga", vertebrado=True),
        Animal(nome="Michelangelo", especie="Tartaruga", vertebrado=True),
        Animal(nome="Splinter", especie="Rato", vertebrado=True),
    ]

    animais.append(Animal(nome="Bruce Wayne", especie="Humano", vertebrado=True))

    # 2. -----------------------------------------------------------------------
    _desenvolvedor = {
        "nome": "Pedro",
        "idade": 23,
        "hobby": "artista",
    }

    # 3. -----------------------------------------------------------------------
    _dias_da_semana = (
        "domingo",
        "segunda",
        "terca",
        "quarta",
        "quinta",
        "sexta",
        "sabado",
    )


if __name__ == "__main__":
    main()
