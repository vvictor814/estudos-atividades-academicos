#desafio prático 3

#questão 1
idades = []
for i in range(10):
    idades.append(int(input(f"Digite a idade {i + 1 }: ")))

print(f"\nIdades: {idades}")

media = sum(idades) / len(idades)
print(f"A média das idades é: {media:.2f}.")

ordenadas = sorted(idades)
meio = len(ordenadas) // 2

if len(ordenadas) % 2 == 0:
    mediana = (ordenadas[meio - 1] + ordenadas[meio]) / 2
else:
    mediana = ordenadas[meio]

print(f"A mediana é: {mediana}.")

maior_freq = 0
for idade in idades:
    freq = idades.count(idade)
    if freq > maior_freq:
        maior_freq = freq

if maior_freq == 1:
    print("Não há moda, nenhum valor se repete.")
else:
    modas = []
    for idade in idades:
        if idades.count(idade) == maior_freq and idade not in modas:
            modas.append(idade)
    print(f"Moda: {modas}.")

#questão 2
bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul", "vermelha", "verde", "azul", "vermelha"]

total = len(bolas)

vermelhas = bolas.count("vermelha")

probabilidade = vermelhas / total

a, b = vermelhas,total
while b != 0:
    a, b = b, a % b
mdc = a

num = vermelhas // mdc
den = total // mdc

print(f"Total de bolas na caixa: {total}")
print(f"Bolas vermelhas: {vermelhas}")
print(f"Probabilidade: {probabilidade}")
print(f"Fração: {vermelhas}/{total} = {num}/{den}")
print(f"Porcentagem: {probabilidade * 100:.0f}%")

#questão 3
alunos = [
    ["Ana", 7.5, 8.0, 9.0],
    ["Bruno", 6.0, 5.5, 7.0],
    ["Carlos", 9.0, 8.5, 10.0],
    ["Daniela", 5.0, 6.0, 4.5],
    ["Eduardo", 8.0, 7.5, 6.5],
]

MEDIA_MINIMA = 7.0
medias = []
aprovados = 0
reprovados = 0

print("=== RELATÓRIO DA TURMA ===")
for aluno in alunos:
    nome = aluno[0]
    media = (aluno[1] + aluno[2] + aluno[3]) / 3
    medias.append(media)

    if media >= MEDIA_MINIMA:
        situacao = "Aprovado"
        aprovados += 1
    else:
        situacao = "Reprovado"
        reprovados += 1

    print(f"Aluno: {nome:<8} | Média: {media:.2f} | Situação: {situacao}")

media_geral = sum(medias) / len(medias)
maior = medias.index(max(medias))
menor = medias.index(min(medias))

print("\n--- Resumo ---")
print(f"Média geral da turma: {media_geral:.2f}")
print(f"Maior média: {alunos[maior][0]} ({medias[maior]:.2f})")
print(f"Menor média: {alunos[menor][0]} ({medias[menor]:.2f})")
print(f"Aprovados: {aprovados}")
print(f"Reprovados: {reprovados}")

#questão 4
precos = [50, 80, 120, 35, 200, 75]

novos_precos = [round(preco * 1.10, 2) for preco in precos]

print(novos_precos)

#questão 5
def calcular_valor(horas):
    if horas <= 1:
        return 5.00
    elif horas <= 3:
        return 10.00
    elif horas <= 5:
        return 15.00
    else:
        return 20.00

placa = input("Placa do veículo: ")
horas = float(input("Tempo de permanência (em horas): "))

valor = calcular_valor(horas)

print(f"\nVeículo: {placa}")
print(f"Tempo: {horas:.1f} hora(s)")
print(f"Valor a pagar: R$ {valor:.2f}")

#questão 6
def calcular_idade(ano_nascimento, ano_atual):
    return ano_atual - ano_nascimento


ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

idade = calcular_idade(ano_nascimento, ano_atual)
print(f"Idade: {idade} anos")

if idade >= 18:
    print("A pessoa é maior de idade.")
else:
    print("A pessoa é menor de idade.")

#questão 7
def area_triangulo(base, altura):
    return (base * altura) / 2


def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2


def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2

print("Área do triângulo")
base = float(input("Base: "))
altura = float(input("Altura: "))
print(f"  Área = {area_triangulo(base, altura):.2f}\n")

print("Área do trapézio")
base_maior = float(input("Base maior: "))
base_menor = float(input("Base menor: "))
altura = float(input("  Altura: "))
print(f"  Área = {area_trapezio(base_maior, base_menor, altura):.2f}\n")

print("Área do losango")
diagonal_maior = float(input("Diagonal maior: "))
diagonal_menor = float(input("Diagonal menor: "))
print(f"Área = {area_losango(diagonal_maior, diagonal_menor):.2f}")

#questão 8
def senha_valida(senha):
    return len(senha) >= 8

def validar_senha_desafio(senha):
    tem_tamanho_minimo = len(senha) >= 8
    tem_numero = any(caractere.isdigit() for caractere in senha)
    
    return tem_tamanho_minimo and tem_numero