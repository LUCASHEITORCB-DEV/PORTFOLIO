def Soma(A, B):
    return A + B

def Subt(A, B):
    return A - B

def Divi(A, B):
    if B == 0:
        return "Erro Não é possível Dividir Por Zero"
    else:
        return A / B

def Multi(A, B):
    return A * B

def Calculadora():
    Operac = (input('Digite Uma Operação 4 Operações Básicas +, -, /, *: '))
    Num1 =  float(input('Digite o 1 Número: '))
    Num2 = float(input('Digite o 2 Número: '))

    if Operac == '+':
        resultado = Soma(Num1, Num2)
    elif Operac == '-':
        resultado = Subt(Num1, Num2)
    elif Operac == '*':
        resultado = Multi(Num1, Num2)
    else:
        Operac == '/'
        resultado = Divi(Num1, Num2)

    print(f'Resultado: {resultado}')
Calculadora()

#⚠️ Código feito nos meus primeiros dias estudando Python.