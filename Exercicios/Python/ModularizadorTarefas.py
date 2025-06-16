# 1. Verificar se um ano é bissexto. Um ano é bissexto se for múltiplo de 4, mas não
# de 100, exceto se for múltiplo de 400. Peça ao usuário um ano e verifique se ele é
# bissexto.

def Ano():
    while True:
        try:
            ano = int(input("Digite O Ano: "))
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                return f'O Ano é Bissexto'
            else:
                return f'o Ano não é Bissexto'
        except ValueError:
            print("Digite Apenas Números")
            continue

# 2. Classificação de idade. Peça a idade do usuário e classifique-o conforme a tabela:
# A. 0 a 12 anos → Criança
# B. 13 a 17 anos → Adolescente
# C. 18 a 59 anos → Adulto
# D. 60 anos ou mais → Idoso

def Idade():
    while True: #loop se encerra ao Digitar Apenas Números
        
        try:
            Idade = int(input("Digite A Sua Idade: "))

            if  0 <= Idade <=12:
                return f'Você tem {Idade} e é Criança'
            elif 13 <= Idade <=17:
                return f'Você tem {Idade} e é Adolescente'
            elif 18 <= Idade <=59:
                return f'Você tem {Idade} e é Adulto'
            else:
                return f'Você tem {Idade} e é Idoso'
        
        except ValueError:
            print('Digite Apenas Números')
            continue

# 3. Cálculo do preço com desconto. Peça o valor de um produto ao usuário e aplique
# um desconto baseado no valor:
# Até R$ 100,00 → Sem desconto
# De R$ 100,01 a R$ 500,00 → 10% de desconto
# Acima de R$ 500,00 → 20% de desconto

def Valor_Do_Produto():
    Valor_Do_Produto = float(input("Digite O Valor Do Produto: "))
    if Valor_Do_Produto <= 100:
        print('VALOR SEM DESCONTO')
    elif 100 > Valor_Do_Produto <= 500 :
        Desconto1 = 0.10
        print(f'Valor é {Valor_Do_Produto - Valor_Do_Produto * Desconto1}')
    elif Valor_Do_Produto >= 500:
        Desconto2 = 0.20
        print(f'{Valor_Do_Produto - Valor_Do_Produto * Desconto2}')

# 4. Calculadora de IMC. Peça o peso e a altura do usuário e calcule o Índice de Massa
# Corporal (IMC), classificando o resultado conforme a tabela:
# • Abaixo de 18,5 → Abaixo do peso
# • 18,5 a 24,9 → Peso normal
# • 25,0 a 29,9 → Sobrepeso
# • 30,0 a 34,9 → Obesidade grau 1
# • 35,0 a 39,9 → Obesidade grau 2
# • 40 ou mais → Obesidade grau 3

def Calcular():
    altura = float(input("Digite Sua Altura: "))
    peso = float(input("Digite Seu Peso: "))
    imc = peso / (altura * altura)

    if imc < 18.5:
        return f'Seu Imc é {imc:2f} Você está Abaixo do Peso'
    elif 18.5 <= imc <= 24.9:
        return f'Seu Imc é {imc:2f} Você está Peso Normal'
    elif 25.0 <= imc <= 29.9:
         return f'Seu Imc é {imc:2f} Você SobrePeso'
    elif 30.0 <= imc <= 34.9:
        return f'Seu Imc é {imc:2f} Obesidade Grau I'
    elif 35.0 <= imc <= 39.9:
        return f'Seu Imc é {imc:2f} Obesidade Grau II'
    else: 
        return f'Seu Imc é {imc:2f} Obesidade Grau III'

# 5. Classificação do Índice de Eficiência de Produção. Em um processo industrial, a
# eficiência da produção é avaliada com base na relação entre a produção real e a
# produção planejada. Crie um programa que peça ao usuário a quantidade
# planejada e a quantidade produzida, calcule a eficiência (%) e classifique o
# desempenho conforme a tabela:
# • Acima de 100% → Superprodução
# • Entre 90% e 100% → Produção eficiente
# • Entre 75% e 89% → Produção aceitável
# • Abaixo de 75% → Produção ineficiente

def Quantia_Produzida():
    quantidade_planejada = float(input("Digite a quantidade planejada: "))
    quantidade_produzida = float(input("Digite a quantidade produzida: "))

    eficiencia = (quantidade_produzida / quantidade_planejada) * 100

    if eficiencia > 100:
        classificacao = "Superprodução"
    elif 90 <= eficiencia <= 100:
        classificacao = "Produção eficiente"
    elif 75 <= eficiencia < 90:
        classificacao = "Produção aceitável"
    else:
        classificacao = "Produção ineficiente"

print("Escolha Uma Tarefa Para Chamar entre Ano, Calcular, Idade, Quantia_Produzida, Valor_Produto ")
Escolha = input("Escolha A Tarefa: ").lower()

if Escolha == 'ano':
    print(Ano())
elif Escolha == 'idade':
    print(Idade())
elif Escolha == 'quantia_Produzida':
    print(Quantia_Produzida())
elif Escolha == 'calcular':
    print(Calcular())