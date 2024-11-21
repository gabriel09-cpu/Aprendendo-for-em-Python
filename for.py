"""notas = [10,8,7,5,9]

for i in notas:
    print(i)"""

"""texto = "python"
for caractere in texto:
    print(caractere)"""

"""for caractere in "python":
    if caractere == "y":
        print("i")
        continue
    print(caractere)"""
 
 # função range
"""for numero in range(3):
    print(numero)"""

"""for gol in range(1,7,2):
    print("Gol da Alemanha!")
print("Gol da Brasil")

for i in range(1000):
    print("gol da alemanha")
    if i == 6:
        break
    print("Gol do Brasil, Vai Brasil!!!")"""

#Usando o else depois do for
"""for numero in [10,7,9,5]:
    print(f"Número: {numero}")
    if numero == 9:
        break
else:
    print("Acabou!")"""

qtd_alunos = int(input("Digite a quantidade de alunos da sala: "))
total = 0
for aluno in range(qtd_alunos):
    nota = float(input(f"Digite a notado aluno {aluno+1}°: "))
    total += nota
print(f"A média da turma é {total/qtd_alunos: .2f}")
