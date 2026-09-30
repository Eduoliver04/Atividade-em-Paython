def soma (a,b ):
    somar = a + b
    return somar 
def subtrair(a,b ):
    return a - b 
if __name__ == '__main__':
    operacao = input('Digite o que queira calcular (+ ou -):')
    numero1 = int(input('Digite o primeiro valor inteiro: '))
    numero2 = int(input('Digite o segundo valor inteiro: '))
    if operacao == '+':
        retorno_soma = soma(numero1, numero2)
        print(f'soma = {retorno_soma}')
    elif operacao == '-':
    
        print(f'Subtração = {subtrair(numero1, numero2)}')
    else:
        print('NOME DE OPERAÇÃO INCORRETA!!')