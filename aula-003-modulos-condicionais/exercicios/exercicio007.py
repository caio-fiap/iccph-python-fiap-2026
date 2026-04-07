# receber ano de nasc e indicar se o voto é opicional

ano_nasc = int(input("Digite seu ano de nascimento: "))

if 2026 - ano_nasc < 16:
    print("Você não pode votar")
elif 70 > 2026 - ano_nasc >= 18:
    print("Você é obrigado a votar")
else:
    print("Você não é obrigado a votar")