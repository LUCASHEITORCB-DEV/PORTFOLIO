"""Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23."""

horas = input('Digite as Horas: ')

try:
    horas1 = int(horas)
    if horas1 >=0 and horas1 <=11:
        print('Bom Dia ')
    elif horas1 >=12 and horas1 <=17:
        print('Boa Tarde ')
    elif horas1 >18 and horas1 <=23:
        print('Boa Noite ')
    else:
        print('Não é válido: ')

except:
    print('Não é Válido')

#⚠️ Código feito nos meus primeiros dias estudando Python.