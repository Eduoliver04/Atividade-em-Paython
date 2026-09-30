numero1 = int(input('Digite o primeito numero: '))
numero2 = int(input('Digite o segundo numero: '))
numero3 = int(input('Digite o terceiro numero: '))

maior = numero1
if (numero2 > maior):
    maior = numero2
if (numero3 > maior):
    maior = numero3

print(f'O maior numero digitado é: {maior}!')

