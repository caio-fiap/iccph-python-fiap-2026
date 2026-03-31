# receber idade e indicar se o voto é opicional

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você não pode votar")
elif 70 > idade >= 18:
    print("Você é obrigado a votar")
else:
    print("Você não é obrigado a votar")