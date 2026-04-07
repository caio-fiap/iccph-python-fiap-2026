#recebe dois numeros e indica qual o maior (ou se sao iguais)

num_a = float(input("Informe um número: "))
num_b = float(input("Informe outro número: "))

if num_a > num_b:
    print(f"Maior: {num_a}")
elif num_b > num_a:
    print(f"Maior: {num_b}")
else:
    print("Os números são iguais")