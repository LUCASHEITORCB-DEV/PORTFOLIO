import os

print('Calculadora Básica')

while True:

    Entrada = input('Deseja Entrar Aperte S/N?: ').lower()
    if Entrada == 'N' and 'n':
        print('Você Saiu: ')
        break

    Ope = input('Deseja Limpar a Tela Digite S: ')
    if Ope == 's' or Ope == 'S':
        os.system('cls')
        print('Você Limpou')

    Int_Num1 = input('Digite Um Número Inicial ')
    Int_Num2 = input('Digite o Segundo Número ')
    Int_Ope = input('Escolha a Operação ')

    try:
        
        Int_Dig1 = float(Int_Num1)
        Int_Dig2 = float(Int_Num2)

        if Int_Ope == '+':
            print(Int_Dig1 + Int_Dig2)
        if Int_Ope == '-':
            print(Int_Dig1 - Int_Dig2)
        if Int_Ope == '/':
            print(Int_Dig1 / Int_Dig2)
        if Int_Ope == '*':
            print(Int_Dig1 * Int_Dig2)

    except ZeroDivisionError:
        print('Não é possivel dividir por zero')
    except ValueError:
        print('Não é possivel somar Letras')

#⚠️ Código feito nos meus primeiros dias estudando Python.