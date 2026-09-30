def converte_em_minutos(horas, minutos):
    horas1 = (horas * 60) + minutos
    return print(f'Horario convertido a minutos é: {horas1}')
if __name__ =='__main__':
    horas = int(input('Digite a hora:'))
    minutos = int(input('Digite os minutos: '))
    converte_em_minutos(horas, minutos)