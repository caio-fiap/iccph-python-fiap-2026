#leitura de quatro notas. calcular a media e indicar se o aluno foi aprovado, reprovado ou recuperação.
#media < 5 - reprovado; 5 <= media < 7 - rec; media > 7 - aprovado

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 5:
    print("Reprovado!")
elif 5 <= media < 7:
    print("Recuperação!")
else:
    print("Aprovado")


