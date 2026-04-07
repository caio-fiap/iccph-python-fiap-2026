#le dois valores inteiros, mostra se sao multiplos ou nao

num_a = int(input("Número 1: "))
num_b = int(input("Número 2: "))

if num_a % num_b == 0 or num_b % num_a == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")