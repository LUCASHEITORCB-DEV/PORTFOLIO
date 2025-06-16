# Crie um programa que peça o consumo de energia elétrica (kWh) e calcule
# o valor da conta com base na tabela:

def KWH():
    try:
        a = float(input("Digite O Consumo Em Kwh: "))
        if a <= 100:
            return f'Valor R${a * 0.50:2f}'
        elif 101 <= a <= 300:
            return f'Valor R${a * 0.70:2f}'
        elif a > 300:
            return f'Valor R${a * 0.90:2f}' 
    except ValueError:
        return f'Erro! Digite Apenas Números'
    
print(KWH())        
#⚠️ Código feito nos meus primeiros dias estudando Python.