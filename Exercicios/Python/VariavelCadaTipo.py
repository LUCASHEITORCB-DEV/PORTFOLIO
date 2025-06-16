#Fazer váriavel primitiva de cada tipo

while True:

    Str1 = input('Digite Uma Variável Seu Nome: ')

    if Str1 in '1234567890':
        print('Digite Somente Letras Válida')
        continue

    Int1 = input('Digite Sua Idade Do Tipo Inteiro: ')

    if '1234567890' in Int1:    
        print('Digite Um Número Válido')
        continue

    Bool1 = input('Digite Uma Variável Do Tipo Verdadeiro Ou Falso: ')
    if Bool1 == '4' or Bool1 == '4':
        print('Seu Bool É Verdadeiro')
    else:
        print('Seu Bool É Falso')

    Float1 = input('Digite Uma Variável De Números Decimais: ')

    Float_TT = float(Float1)

    print(f'Sua String é {Str1} Seu Número Inteiro {Int1} Seu Bool é Do Tipo {Bool1} Seu Float é {Float_TT:4f}')
    break

#⚠️ Código feito nos meu primeiro mês estudando Python.