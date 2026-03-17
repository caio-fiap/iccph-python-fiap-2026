print("="*10, "atividade", "="*10)

print("\nDesafio 1: \n")
nome = input("Digite seu nome: ")
print(f"Bem vindo, {nome}")

print("\nDesafio 2: \n")
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if dia > 31:
    print("Dia inválido")
elif dia < 10:
    dia = '0' + str(dia)

if mes > 12 or mes < 0:
    print("Mês inválido")
elif mes < 10:
    mes = '0' + str(mes)

print(f"A data é: {dia}/{mes}/{ano}")

print("\nDesafio 3: \n")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print(f"A soma entre {num1} e {num2} é: {num1 + num2}")