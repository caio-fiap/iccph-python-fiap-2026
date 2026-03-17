'''Neste problema, deve-se ler o nome de uma peça que chamaremos de peça1, o número de peças1 que
o usuário quer, o valor unitário de cada peça1, o nome de uma peça2, o número de peças2 e o valor
unitário de cada peça2. Após, calcule e mostre o valor a ser pago'''
from jinja2.nodes import Continue
from sympy.codegen.ast import continue_

print("=" * 10, "Exercício 8", "=" * 10)

print("\nTotal a ser pago\n")


nome1 = input("Nome da peça 1: ")
qtd1 = int(input("Quantidade de peças: "))
valor1 = float(input("Valor unitário da peça: "))
preco1 = qtd1 * valor1

while True:
    nome2 = input("\nNome da peça 2: ")
    if nome2 == nome1:
        print("As peças não podem ser a mesma")
        continue
    qtd2 = int(input("Quantidade de peças: "))
    valor2 = float(input("Valor unitário da peça: "))
    preco2 = qtd2 * valor2
    break

print(f"\nO total a ser pago é: R$ {preco1 + preco2:.2f}")

