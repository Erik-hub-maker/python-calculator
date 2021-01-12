#Calculadora
################## 
#Pedir o nome do usuário
nome = str(input('Olá, qual é o seu nome?'))

#Perguntar Qual operação ele vai fazer
operacao = str(input('Escolha a operação que deseja realizar(+,-,*,/): '))

#Pedir o primeiro e o segundo número
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

#Realizar as operações necessárias
if operacao == '+':
    soma = n1 + n2
    print('{} a soma entre {} e {} é: {}'.format(nome, n1, n2, soma))
elif operacao == '-':
    sub = n1 - n2 
    print('{} a subtração entre {} e {} é: {}'.format(nome, n1, n2, sub))
elif operacao == '*':
    mult = n1 * n2
    print('{} a multiplicação entre {} e {} é: {}'.format(nome, n1, n2, mult))
else:
    div = n1 / n2
    print('{} a divisão entre {} e {} é: {}'.format(nome, n1, n2, div))
