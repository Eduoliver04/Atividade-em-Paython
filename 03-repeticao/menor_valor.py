ct = 0
menor_valor =999999999
print('Digite (0) para sair! ')
while True:
    numero = int(input('Digite seu numero: '))
    if numero == 0:
        break
    if numero < menor_valor:
        menor_valor = numero
print(f'O menor valor digitado é:{menor_valor}')

