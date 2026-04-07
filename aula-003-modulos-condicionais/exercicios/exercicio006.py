#recebe dois numeros e um caractere representando operção (+, -, *, /)

def operacao(num_a, num_b, op):
    if op == '+':
        resultado = num_a + num_b
    if op == '-':
        resultado = num_a - num_b
    if op == '*':
        resultado = num_a * num_b
    if op == '/':
        resultado = num_a / num_b

    return resultado

num_2 = int(input("Numero 1: "))
num_1 = int(input("Numero 2: "))
sinal = (input("Operação desejada (+, -, *, /): "))
print(operacao(num_1, num_2, sinal))