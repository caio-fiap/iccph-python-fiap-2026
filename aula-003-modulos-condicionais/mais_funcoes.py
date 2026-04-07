#função com parametro e sem retorno
def boas_vindas(nome):
    print(f"Olá {nome}! Seja bem vindo!")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)
print(f"{type(nome_digitado)}\n")

#função com parametro e COM retorno
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma = soma(5, 9)
print(f"{resultado_soma}")
print(f"{type(soma)}\n")

def raiz (a, b):
    raiz = a ** (1 / b)
    return raiz

print(f"{raiz(27, 3)}")