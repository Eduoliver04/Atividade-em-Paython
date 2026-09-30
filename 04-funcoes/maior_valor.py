def maximo (numero1, numero2 ):
    if numero1 > numero2:
        return numero1
    elif numero1 == numero2:
        return numero1
    else:
        return numero2 
if __name__ == '__main__':
    numero1 = int(input('Digite o primeiro valor: '))
    numero2 = int(input('Digite o segundo valor: '))
    Mv_retorno = maximo(numero1, numero2)
    print(F'O maior valor digitado é: {Mv_retorno}')