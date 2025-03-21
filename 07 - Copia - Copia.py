print('Ola, seja bem vindo ao nosso site:\n ')
nome = input('Digite o seu nome:')
print(f'{nome}, hoje vamos descobrir o seu IMC\n')
altura =float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc= peso/altura**2

if imc<18.5:
    print(f'Voce esta abaixo do peso {round(imc,3)}')
elif imc >= 18.5 and imc <24.99:
    print(f'Voce esta no seu peso normal {round(imc,3)}')
elif imc >= 24.99 and imc <29.99:
    print(f'Voce esta com sobrepeso {round(imc,3)}')
else:
    print(f'Voce esta com obesidade {round(imc,3)}')
