qtd_pessoas = int(input("Informe a quantidade de participantes: "))
total_m = 0

for pessoas in range(qtd_pessoas):
    sexo = str(input(f"Pessoa {pessoas+1} nforme seu sexo: ")).upper()
    if sexo == "M":
        total_m = total_m + 1
print(f"Tem {total_m} homens!")




