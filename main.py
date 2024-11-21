#Mostrar Tabuada
num = int(input("Informe o número: "))
for i in range(0,11):
    resultado = num * i
    print(f"{num}x{i} = {resultado}")