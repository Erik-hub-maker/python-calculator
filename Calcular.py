#Calculadora feita em python

#pedir o nome do usuário
nome = str(input("Qual é o seu nome? "))

#Pedir a operação que ele deseja realizar
operação = str(input("Qual das quatro operação você deseja realizar?"))
operação = operação.upper()

#Pedir os dois números para realizar a operação
n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))

#Realizar as operações necessárias
if operação == "MAIS":
    soma = n1 + n2
    print("{} a soma entre {} e {} é {}".format(nome, n1, n2, soma))
elif "SUBTRAÇÃO":
    sub = n1 - n2
    print("{} a subtração entre {} e {} é {}".format(nome, n1, n2, sub))
elif "MULTIPLICAÇÃO":
    mult = n1 * n2
    print("{} a multiplicação entre {} e {} é {}".format(nome, n1, n2, mult))
elif "DIVISÃO":
    div = n1 / n2
    print("{} a divisão entre {} e {} é {}".format(nome, n1, n2, div))
else:
    print("Operação inválida")
