ct = 0
soma = 0
print('Digite (-1) para sair! ')
while True:
    numero = int(input('Digite um numero: '))
    if numero == -1:
        break
    ct= ct +1
    soma= soma + numero
print(f'A quantidade de numeros é: {ct}')
print(f'A soma dos numeros é: {soma}')
