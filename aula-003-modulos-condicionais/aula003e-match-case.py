escolha_user = 1
# 0 -> sair do programa
# 1 -> entrar no programa
# resto -> erro

match escolha_user:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro!!!")