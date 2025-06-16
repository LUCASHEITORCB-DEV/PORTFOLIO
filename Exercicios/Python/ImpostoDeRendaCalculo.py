# Faça um programa que peça o salário bruto do usuário e calcule o Imposto
# de Renda conforme a tabela abaixo:

def Salario():
    while True: #Loop Apenas Para O Tratamento De Erros E Logo Em Seguida Se Encerrar
        try:
            Salario1 = float(input("Digite Seu Salário: "))
            if Salario1 <= 2000:
                return "Você Está Isento de Imposto: "

            elif  2001 <= Salario1 <= 3500:
                imposto_35 = 0.075 * Salario1
                return f'Terá de Pagar R${imposto_35}'

            elif 3501 <= Salario1 <= 5000:
                imposto301 = 0.15 * Salario1
                return f'Terá de Pagar R${imposto301}'

            elif Salario1 > 5000:
                imposto50 = 0.225 * Salario1
                return f'Terá de Pagar: R${imposto50}'

        except ValueError:
            print("Digite Apenas Números")
            continue
print(Salario())