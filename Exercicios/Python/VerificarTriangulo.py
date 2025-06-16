"""Escreva um programa que leia três 
lados de um triângulo e determine seu tipo"""

def LadoTriangulos():
    while True:
        print("Digite os Lados Do Triângulo: ")
        a = int(input("Digite O 1° Lado Do Triangulo: "))
        b = int(input("Digite O 2° Lado Do Triangulo: "))
        c = int(input("Digite O 3° Lado Do Triangulo: "))
        if a + b <= c or a + c <= b or b + c <= a:
            print("Digite Valores Corretos Não é Um Triângulo\n\n\n")
            continue
        elif a == b == c:
            return 'Seu Triângulo é Equilátero'
        elif a == b != c or a == c != b or c == b != a: #Verifica Dois Lados Diferentes Do Triângulo
            return 'Seu Triângulo é Isoceles'
        else:
            return 'Seu Triângulo é Escaleno'
        
print(LadoTriangulos())

#⚠️ Código feito nos meus primeiros dias estudando Python.