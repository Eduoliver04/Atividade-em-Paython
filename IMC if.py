nome = input('Seja bem vindo ao nosso site!\n Qual é o seu nome?')
print(f'Ola {nome} hoje vamos descobrir qual é o seu IMC!')
peso = float(input('Digite seu peso?'))
altura = float(input('Qual é a sua altura?'))

imc = peso / altura ** 2
if imc <=18.5:
    print(f'Seu imc é {imc} Voce esta abaixo do peso')
elif imc >18.5 and imc <= 24.99:
    print(f'Seu imc é {imc} Voce esta no seu peso normal')
elif imc >25 and imc <= 29.99:
    print(f'Seu imc é {imc} Voce esta com sobrepeso')
else:
    print(f'Seu imc é {imc}Voce esta com Obesidade')
print(f'Muito obrigado pela sua visita, volte novamente!')


