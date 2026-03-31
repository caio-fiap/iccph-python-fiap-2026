# // -> divisão inteira
from sqlalchemy.sql.operators import truediv

num1 = 5
num2 = 2

print(type(num1), type(num2))

resultado = num1 / num2
print(resultado, type(resultado))

#operadores de atribuição

num = 15
print()
print(num)

num = num + 2 # acumulador
print(num)

num += 2
print(num)
print()

# operadores relacionais
# = -> recebe; == -> igual a

print (6 == 2) # retorna true ou false

idade = 18
print (idade >= 21)

print()

logado = True
print(logado, type(logado))

maior_idade = idade >= 18
print(maior_idade, type(maior_idade))
print()

# strings

nome1 = "Marcos"
nome2 = "marcos"

print(nome1.upper() == nome2.upper())
