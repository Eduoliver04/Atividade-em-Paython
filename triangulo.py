a = float(input('Qual o comprimento de A: '))
b = float(input('Qual o comprimento de B: '))
c = float(input('Qual o comprimento de C: '))
    if a + b > c and a + c > b and b + c > a:

        if a == b == c:
            print("Triângulo Equilátero")
        elif a == b or a == c or b == c:
            print("Triângulo Isósceles")
        else:
           print("Triângulo Escaleno")
    else:
        print("Os valores informados não formam um triângulo")