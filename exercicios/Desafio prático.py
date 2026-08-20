#1. Verificador de Par ou Ímpar. Peça ao usuário um número inteiro e diga se ele é par ou ímpar.
print(
    "Olá, usuário(a)!"
    "\nEsta ferramenta determina se um número é par ou ímpar.")

numero = int(input("\nDigite um número inteiro qualquer para saber se ele é par ou ímpar: "))

if numero % 2 == 0:
    print(f"O número digitado ({numero}) é par.")
else:
    print(f"O número digitado ({numero}) é ímpar.")

#2. Classificador de Idade. Solicite a idade de uma pessoa. Classifique-a como "Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso" (65 anos ou mais). 
idade_usuario = int(input("\nInforme sua idade: "))

if 0 <= idade_usuario <= 12:
    print("Faixa etária identificada: 'Criança'.")
elif 13 <= idade_usuario <= 17:
    print("Faixa etária identificada: 'Adolescente'.")
elif 18 <= idade_usuario <= 64:
    print("Faixa etária identificada: 'Adulto'.")
elif idade_usuario >= 65:
    print("Faixa etária identificada: 'Idoso'.")
else:
    print("Idade digitada inválida.")

#3. Mini Calculadora. Crie uma mini calculadora que permita ao usuário escolher entre as operações de soma, subtração, multiplicação e divisão. Peça dois números e a operação desejada. Imprima o resultado. 
print("\nCalculadora 4bA: 4 operações básicas da aritmética.")
print(
    "\nAviso: esta calculadora, como o nome sugere, só calcula soma, subtração, multiplicação e divisão"
    "\nalém de só conseguir operar uma conta por vez, com no máximo dois números.")

n1 = float(input("\nInsira o primeiro número: "))
operacao = input("Agora selecione uma operação entre os números: (+, -, * ou /): ")
n2 = float(input("Insira o segundo número: "))

if operacao == "+":
    resultado = n1 + n2
elif operacao == "-":
    resultado = n1 - n2
elif operacao == "*": 
    resultado = n1 * n2
elif operacao == "/": 
    resultado = n1 / n2
else:
    print("Caracter inválido. Reinicie a calculadora e refaça a operação.")
print(f"Resultado: {resultado}")

#4. Classificador de Triângulos. Peça ao usuário para digitar o comprimento de três lados de um triângulo. Determine se os lados formam um triângulo válido e, em caso afirmativo, classifique-o como Equilátero, Isósceles ou Escaleno.
print("\nFerramenta de classificação de triângulos de acordo com a medida de seus lados.")

lado_a = int(input("Considerando que todos os lados já estão na mesma unidade de medida, informe a medida de um dos lados: "))
lado_b = int(input("Agora outro lado diferente do primeiro: "))
lado_c = int(input("Por fim, o lado que ainda não foi inserido: "))

if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
    print("\nO triângulo existe, prossigamos com sua classicação:")
    if lado_a == lado_b and lado_b == lado_c:
        print("Equilátero.")
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        print("Isósceles.")
    else:
        print("Escaleno.")
else:
    print("\nO triângulo inserido não existe, reveja seus dados.")

#5. Solicite os coeficientes a, b e c de uma equação do segundo grau (ax² + bx + c = 0). Determine e mostre o número de raízes reais distintas que a equação possui.
print("\nFerramenta que determina o número de raizes reais distintas de uma equação do segundo grau.")
a = float(input("Digite o coeficiente quadrático da equação (a): "))
while a == 0:
    print("Se a = 0, a equação não é de segundo grau.")
    a = float(input("Digite novamente o coeficiente quadrático (a): "))
b = float(input("Digite o coeficiente linear da equação (b): "))
c = float(input("Digite o termo independente da equação (c): "))

delta = -b**2 - 4 * a * c

if delta > 0:
    print("\nHá duas raízes reais distintas.")
elif delta == 0:
    print("\nHá uma raiz real.")
else:
    print("\nNão há nenhuma raiz real.")

#6. Peça ao usuário a temperatura da água (em graus Celsius). Determine o estado físico da água (sólido, líquido ou gasoso)
print("\nDeterminando o estado físico da água de acordo com a temperatura informada, considerando 1 atm de pressão.")

temperatura_agua = float(input("Informe a temperatura da água em graus Celcius (troque as vírgulas por pontos): "))

if temperatura_agua <= 0:
    print("\nA água está em estado sólido.")
elif 0 < temperatura_agua < 100: 
    print("\nA água está em estado líguido.")
else:
    print("\nA água está em estado gasoso.")

#7. Uma empresa de vendas possui corretores. A empresa paga ao corretor uma comissão calculada de acordo com o valor de suas vendas. Se o valor da venda de um corretor for até R$ 500.000 a comissão será de 6% do valor vendido. Se o valor da venda do corretor estiver acima de R$ 500.000 até R$ 700.000 a comissão será de 8.5%. Se o valor da venda do corretor estiver acima de R$ 700.000 até R$ 1.000.000 a comissão será de 10%. Se o valor da venda de um corretor for maior que R$ 1.000.000 a comissão será de 12% do valor vendido. Escreva um código que imprima um relatório contendo o nome, valor da venda e a comissão do corretor. 

nome_corretor = input("\nNome do(a) corretor(a): ")

valor_venda = float(input("Informe o valor da venda: "))

if 0 <= valor_venda <= 500000:
    print(
        f"NOME: {nome_corretor}"
        f"\nVALOR_VENDA: R${valor_venda}"
        f"\nCOMISSÃO: R${valor_venda * 0.06}.")
elif 500000 < valor_venda <= 700000:
    print(
        f"NOME: {nome_corretor}"
        f"\nVALOR_VENDA: R${valor_venda}"
        f"\nCOMISSÃO: R${valor_venda * 0.085}.")
elif 700000 < valor_venda <= 1000000:
    print(
        f"NOME: {nome_corretor}"
        f"\nVALOR_VENDA: R${valor_venda}"
        f"\nCOMISSÃO: R${valor_venda * 0.1}.")
elif 1000000 < valor_venda:
    print(
        f"NOME: {nome_corretor}"
        f"\nVALOR_VENDA: R${valor_venda}"
        f"\nCOMISSÃO: R${valor_venda * 0.12}.")
else:
    print("Valores inseridos inválidos, reveja os números informados e insera novamente os dados corrigidos.")

#8. Ajude um hotel da cidade a calcular o valor da hospedagem. O hotel cobra R$290,00 a diária e mais uma taxa de serviços. A taxa de serviços é de: R$ 6,50 por dia, se o número de diárias for maior que 7; R$ 12,00 por dia, se o número de diárias for igual a 7;R$ 16,50 por diária, se o número de diárias for menor que 7. Você deve pedir a informação de quantos dias o hóspede ficou hospedado. Construa um código que mostre o nome do hóspede e o total da conta a pagar.

nome_hospede = input("\nNome do hóspede: ")
dias_hospedados = int(input("Quantidade de dias hospedados: "))

if dias_hospedados == 7:
    print(f"\n{nome_hospede}, O valor total da hospedagem é de R${290 * dias_hospedados + 12 * dias_hospedados}.")
elif dias_hospedados < 7:
    print(f"\n{nome_hospede}, O valor total da hospedagem é de R${290 * dias_hospedados + 16.5 * dias_hospedados}.")
else: 
    print(f"\n{nome_hospede}, O valor total da hospedagem é de R${290 * dias_hospedados + 6.5 * dias_hospedados}.")