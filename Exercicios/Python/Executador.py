# def Saudacao(nome='Sem Nome'):
#     print(f'Olá,', nome)

# Saudacao('Vinicius')

# def Soma(x, y, z):
#     print(f'{x=} {y=} {z=}','|','x + y + z =', x + y)

# print(Soma)
# print(Soma(y=10, x=15, z=5))


# x = 5
# y = 10

# def escopo():
#     def escopo_2():
#         global x
#         x = 20
#         y = 5
#         print(y)
#     print(x)    
#     escopo_2()

# escopo()   

# def imprimir(nome):
#     return nome

# imprimir('daora')
# imprimir(type(5))
# print(imprimir('Vinicius'))

# def Soma(x):
#     if x > 10:
#         return 'Maior'
#     else:
#         return 'Menor'
    
# Valor = float(input("Valor: "))
# Soma1 = Soma(Valor) 
# print(Soma1)

# def Soma(*args):
#     total = 0
#     for numero in args:
#         total = total + numero
#         print(total)
#         # print(numero)

# a = (Soma(1, 2, 3, 4, 5))
# print(a)

# condicao = False
# passou = None

# if condicao:
#     passou is None
#     print("Passou Mulekote: ")
# else:
#     passou is False
#     print("Não passou")

# def saudacao(msg, *nome):
#     return msg, nome
# def executador(funcao, *args):
#     return funcao(*args)

# a = executador(saudacao, 'Oi', 'eae', 'salve')
# print(a)

# def CriarSaudacao(Msg, Nome):
#     def Saudar():
#         return f'Saudar {Msg} {Nome}'
#     return Saudar

# a = CriarSaudacao('Oi', 'Vinicius')
# print(a())