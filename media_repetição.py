ct = 0
soma = 0
print('Digite (0) para sair! ')
while True:
    nota = int(input('Digite sua nota: '))
    if nota == 0:
        break
    if nota % 2 == 0:
        ct = ct +1
        soma = soma + nota
print('A media é:',  soma/ct)
print(f'Quantidade de alunos: {ct}')