sexo = (input('Qual é o seu sexo? (Homem / Mulher)'))
altura = float(input('Qual é a sua altura? '))
if sexo == 'Homem':
    calculo_homem = (72.7 * altura)- 58
    print(calculo_homem)
elif sexo == 'Mulher':
    calculo_mulher = (62.1* altura)-44.7
    print(calculo_mulher)
else:
    print('Algo deu errado!\nDigite um sexo compativel!')