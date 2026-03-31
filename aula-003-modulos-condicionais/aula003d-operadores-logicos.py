#logica e (and)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

print()

#logica OU (or)

logica_ou = True or False or False
print(logica_ou)

print()

#logica NOT

negacao = not False
print(negacao)

if not verifica_login:
    print("Loga certo")
