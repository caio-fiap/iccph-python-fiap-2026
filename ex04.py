#salario final com base em cargo, hora extra, falta, bonus e desconto

def hora_extra(sal_base, horas):
    extra = horas * (sal_base * .015)
    return extra

def desc_faltas(sal_base, faltas):
    desc = faltas * (sal_base * .02)
    return desc

def bonus(cargo, rebebeu_bonus):
    global val_bonus
    if cargo == 1 and rebebeu_bonus == "s":
        val_bonus = 1000
    if cargo == 2 and rebebeu_bonus == "s":
        val_bonus = 500
    if cargo == 3 and rebebeu_bonus == "s":
        val_bonus = 300
    if cargo == 4 and rebebeu_bonus == "s":
        val_bonus = 100

    return val_bonus

print(f"-" * 10, "CALCULAR SALÁRIO FINAL", "-" * 10, "\n")

print(f"Cargos: \n1 - Gerente\n2 - Analista\n3 - Assistente\n4 - Estagiário\n")

nome = input("Nome do funcionário: ")
cargo = int(input("Cargo do funcionário: "))
sal_base = float(input("Salário base, em R$: "))
horas = int(input("Total de horas extras trabalhadas: "))
faltas = int(input("Total de faltas: "))
recebeu_bonus = input("Recebeu bônus por desempenho (s ou n)? ")

acrescimos = hora_extra(sal_base, horas) + bonus(cargo, recebeu_bonus)
descontos = desc_faltas(sal_base, faltas)
sal_final = sal_base + acrescimos - descontos

print()

print(f"Salário bruto do funcionário {nome.capitalize()}: R${sal_base}")
print(f"Total de acréscimos (horas extras e bônus): R${acrescimos}")
print(f"Total de descontos (faltas): R${descontos}")
print(f"Salário final: R${sal_final}")