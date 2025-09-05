def main():
    # input --------------------------------------------------------------------
    tem_wifi: bool = False
    tem_dados_moveis: bool = True

    # output -------------------------------------------------------------------
    print(f"O celular pode se conectar a internet? {tem_wifi or tem_dados_moveis}")


if __name__ == "__main__":
    main()
