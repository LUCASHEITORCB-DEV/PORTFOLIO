"""Conversor de Unidades
Descrição: Crie um programa que converte unidades, como quilômetros para milhas, Celsius para Fahrenheit, etc.
Conceitos: Funções, operações matemáticas.
Desafio extra: Adicione mais unidades ou permita que o usuário escolha a conversão."""

def conversor_km_to_milha(milha):
    return (milha * 1.609)

def conversor_milha_to_km(milha):
    return (milha / 1.609)
    
while True:
    escolha = int(input("Digite A Unidade A Ser Convertida \n1-KM to Milhas, 2-Milhas To KM,\nObs: Digite Em KM Exp: 10: "))
    if escolha != 1 or escolha != 2:
        print("Digite Valores Válidos: ")
        continue
    valores = float(input("Digite O Valor: "))

    if escolha == '1':
        conversor_km_to_milha(valores)
    elif escolha == '2':
        conversor_milha_to_km(valores)


