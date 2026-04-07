#recebe salario e faz reajuste seguindo criterio

sal = float(input("Salário atual: R$ "))

if sal <= 280:
    per = 20
    aumento = sal * per / 100
    saln = sal + aumento
elif sal < 700:
    per = 15
    aumento = sal * per / 100
    saln = sal + aumento
elif sal < 1500:
    per = 10
    aumento = sal * per / 100
    saln = sal + aumento
else:
    per = 5
    aumento = sal * per / 100
    saln = sal + aumento

print(f"Salário antes do reajuste: R$ {sal}\n\n"
      f"Percentual de aumento: {per}%\n"
      f"Valor de aumento: R$ {aumento}\n"
      f"Salário após reajuste: R$ {saln}\n")
