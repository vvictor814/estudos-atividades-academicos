#Desafio Prático 2

'''1. Utilizando uma estrutura de repetição, escreva um programa em Python que
calcule o fatorial de um número informado pelo usuário.'''

numero = int(input("Digite um número para que seja calculado seu fatorial: "))
fatorial = 1

for fator in range(1, numero + 1):
    fatorial *= fator

print(f"\nO fatorial de {numero} é: {fatorial}")

'''2. Supondo que a população de um país A seja da ordem de 90.000 habitantes
com uma taxa anual de crescimento de 5% e que a população de B seja 200.000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

populacao_a = 90000 
populacao_b = 200000
taxa_crescimento_a = 0.05
taxa_crescimento_b = 0.015
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b

    anos +=1 

print(f"\nSerão necessários {anos} anos para que as populações se igualem ou se ultrapassem.")
print(f"População A final: {populacao_a:.2f} habitantes")
print(f"População B final: {populacao_a:.2f} habitantes")

'''3. Resumo estatístico de notas de um curso. Leia as notas de uma turma até que
o usuário digite algo para sair. Para cada nota válida, determine se o estudante
foi aprovado, ficou em recuperação ou foi reprovado. Considere aprovado para
nota maior ou igual a 7,0, recuperação para nota entre 5,0 e 6,9, e reprovação
para nota inferior a 5,0. Ao final, apresente a média da turma, a maior nota, a menor nota, o percentual
de aprovação e a situação geral da turma. Classifique a turma como “desempenho
satisfatório” quando o percentual de aprovação for igual ou superior a 70%.
Requisitos: utilizar while; aceitar notas entre 0 e 10; não encerrar a leitura ao
receber um valor inválido; impedir divisão por zero; utilizar decisões para a
situação individual e para a classificação geral.'''

print("\nFerramenta de Monitoramento de Desempenho")
print("Para encerrar o uso da ferramenta, digite 'sair'.\n")

soma = 0
quantidade = 0
maior = -1.0 
menor = 11.0
aprovados = 0

while True:

    aluno = input("Nome do aluno: ").strip()

    if aluno.lower() == 'sair': #peguei do Gemini isso do .lower
        break
        
    try:
        nota = float(input("Nota obtida: "))
    except ValueError:
        print("Erro: digite um número válido para a nota.\n")
        continue

    if nota < 0 or nota > 10:
        print("Nota inválida! A nota deve estar entre 0 e 10.\n")
        continue

    soma += nota
    quantidade += 1

    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota

    if nota >= 7.0:
        situacao = "Aprovado"
        aprovados += 1
    elif nota >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"{aluno} - Nota {nota:.2f} - {situacao}.\n")

if quantidade == 0:
    print("\nNenhuma nota válida foi inserida. Encerrando o programa.")
else:
    media = soma / quantidade
    percentual_aprovacao = (aprovados / quantidade) * 100

    if percentual_aprovacao > 70:
        situacao_turma = "Desempenho satisfatório"
    else:
        situacao_turma = "Desempenho insatisfatório"

    print("\n" + "="*30)
    print("RELATÓRIO FINAL")
    print("="*30)
    print(f"Total de alunos: {quantidade}")
    print(f"Média da turma: {media:.2f}")  
    print(f"Maior nota: {maior:.2f}")
    print(f"Menor nota: {menor:.2f}")
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")
    print(f"Situação geral: {situacao_turma}")

'''4. Seleção de atributos para um modelo. Um conjunto de dados possui n atributos
disponíveis. O analista deseja selecionar r atributos para uma etapa de
modelagem, sem considerar a ordem de seleção. Calcule o número de
subconjuntos possíveis usando:
C(n, r) = n! / (r! * (n-r)!)
O programa deve validar 0 <= r <= n e informar se a quantidade de subconjuntos
é compatível com uma busca exaustiva. Considere viável a busca quando houver
até 10.000 combinações.
Requisitos: calcular o resultado sem função pronta de fatorial; utilizar repetição;
aplicar decisões para validar os parâmetros e classificar a viabilidade; explicar
por que a ordem dos atributos não altera uma combinação.'''

#Fui pro além só lendo isso daqui, aqui seria 100% IA...

'''5. Uma população inicial de 2727 indivíduos cresce a uma taxa de 4% ao ano.
Escreva um programa em Python que simule o crescimento dessa população e
mostre o tamanho da população ao final de cada ano, durante 5 anos.'''

populacao = 2727
taxa_crescimento = 0.04

for ano in range(1, 6):
    populacao = populacao * (1 + taxa_crescimento) 
    print(f"\nAno {ano}: {populacao:.2f}")

'''6. Probabilidade experimental. Um experimento consiste em lançar um dado 20
vezes. O programa recebe o resultado de cada lançamento e deve contar quantas
vezes apareceu um número par. Ao final, deve calcular a probabilidade
experimental de obter um número par.'''

import random

total_lancamentos = 20
contador_pares = 0

for lancamentos in range(20):
    resultado = random.randint(1, 6)

    if resultado % 2 == 0:
        contador_pares += 1

    print(f"\nLançamentos {lancamentos + 1}: {resultado}")

probabilidade = (contador_pares / total_lancamentos) * 100

print(f"\nNúmeros pares obtidos: {contador_pares}")
print(f"Probabilidade experimental de sair par: {probabilidade:.2f}%")

#Essa lista aqui tá um desafio dos grandes, achei bem difícil, tive que recorrer a IA para completar quase todas... e abandonei a 4. My bad, ao longo da semana eu vou tentar resolver e atualizar no GitHub.