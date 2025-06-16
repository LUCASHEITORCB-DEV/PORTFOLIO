#Detector de vogais simples

Vogal = input('Digite a Vogal: ').lower()

try:
    if len(Vogal) > 2:
        print('Tem Mais De 2 Letras Digite Apenas Uma Letra')

    elif Vogal in 'aeiou':
            print('Essa Letra é uma vogal')
    elif Vogal not in 'aeiou':
            print ('Essa Letra não é uma vogal')
    
except:
    print('Dígito Inválido')
        
#⚠️ Código feito nos meus primeiros dias estudando Python.