x1 = float(input('Digite a coordenada x do ponto P(x1, y1):'))
y1 = float(input('Digite a coordenada y do ponto P(x1, y1):'))
x2 = float(input('Digite a coordenada x do ponto P(x2, y2):'))
y2 = float(input('Digite a coordenada y do ponto P(x2, y2):'))
distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f'A distância entre os pontos é: {distancia:.2f}')