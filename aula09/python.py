nome = input ("Digite o seu nome").lower()
idade = int(input("Digite a sua idade"))

if (nome == 'Pedro' and idade == 22) or nome == 'drake':
    print("Salve Drake")
elif nome == 'Murilo':
    print("Salve Henrique Hemrique")
else:
    print ("Você não é o Drake")

numero = 0
while numero < 5:
    print(numero)
    numero = numero + 1


lista = ['cubo mágico', 'pagode japonês', 'skate', 'manga com leite']
for item in lista:
    print(item)

for i in range(0,len(lista), 2):
    print(lista[i])