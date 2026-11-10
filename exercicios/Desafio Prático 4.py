#Desafio Prático 4 

'''Jogo de Adivinhação. Utilizando a biblioteca random crie um pequeno jogo de adivinhação de números inteiros que deve ir de 1 a 100. As regras do jogo devem ser:
- Todos os palpites do usuário devem ser armazenados;
- O programa deve informar que o usuário errou o palpite e mostrar uma dica se o
número a ser descoberto é maior ou menor do que o número do palpite;
- Quando o usuário acertar o palpite o programa deve mostrar: todos os números
digitados para o palpite, a quantidade de tentativa.'''

import random # Importando a biblioteca random 

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Lista para armazenar todos os palpites
palpites = []

print("JOGO DE ADIVINHAÇÃO")
print("Tente descobrir o número entre 1 e 100!")

while True:
    tentativa = int(input("Digite seu palpite: "))

    # Armazena o palpite na lista
    palpites.append(tentativa)

    if tentativa < numero_secreto:
        print("Errou! O número secreto é MAIOR.")

    elif tentativa > numero_secreto:
        print("Errou! O número secreto é MENOR.")

    else:
        print("\nParabéns! Você acertou! Não vai ganhar nada...")
        print("O número secreto era:", numero_secreto)

        print("\nTodos os seus palpites:")
        print(palpites)

        print("Quantidade de tentativas:", len(palpites))

        break

'''O professor de matemática Alan Turing pediu sua ajuda para criar um pequeno sistema
para calcular as áreas das figuras planas. Ele pediu que o usuário possa escolher qual figura
quer calcular. Para cada cálculo de uma figura faça uma função específica. Utilize a figura
abaixo como apoio matemático e das figuras que seu programa deve conter. Dica: utilize a
biblioteca math.'''

import math # Importando a biblioteca de matemática

# Função para calcular a área do quadrado
def area_quadrado():
    lado = float(input("\nDigite o lado do quadrado: "))
    area = lado ** 2
    print("Área do quadrado:", area)


# Função para calcular a área do retângulo
def area_retangulo():
    base = float(input("\nDigite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = base * altura
    print("Área do retângulo:", area)


# Função para calcular a área do triângulo
def area_triangulo():
    base = float(input("\nDigite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    print("Área do triângulo:", area)


# Função para calcular a área do círculo
def area_circulo():
    raio = float(input("\nDigite o raio do círculo: "))
    area = math.pi * raio ** 2
    print("Área do círculo:", area)


# Função para calcular a área do trapézio
def area_trapezio():
    base_maior = float(input("\nDigite a base maior: "))
    base_menor = float(input("Digite a base menor: "))
    altura = float(input("Digite a altura do trapézio: "))
    area = ((base_maior + base_menor) * altura) / 2
    print("Área do trapézio:", area)

# Menu principal
while True:
    print("\n===== CALCULADORA DE ÁREAS =====")
    print("1 - Quadrado")
    print("2 - Retângulo")
    print("3 - Triângulo")
    print("4 - Círculo")
    print("5 - Trapézio")
    print("0 - Sair")

    opcao = input("\nEscolha uma figura: ")

    if opcao == "1":
        area_quadrado()

    elif opcao == "2":
        area_retangulo()

    elif opcao == "3":
        area_triangulo()

    elif opcao == "4":
        area_circulo()

    elif opcao == "5":
        area_trapezio()

    elif opcao == "0":
        print("Programa encerrado. Até mais!\n")
        break

    else:
        print("Opção inválida! Tente novamente.")


'''Utilizando função e a bilioteca math crie um programa para calcular as possíveis raízes de
uma equação do 2º grau. Sabendo que: ax² + bx + c = 0. Determine e mostre o número de
raízes reais distintas que a equação possui. Regra: O número de raízes reais depende do
discriminante (delta), Δ = b² - 4ac:
- Δ > 0: Duas raízes reais distintas.
- Δ = 0: Uma raiz real (ou duas raízes reais iguais).
- Δ < 0: Nenhuma raiz real (duas raízes complexas).'''


# Importa a biblioteca math, que permite utilizar funções matemáticas
import math

# Cria uma função para calcular as raízes da equação do 2º grau
def calcular_raizes(a, b, c):

    # Calcula o discriminante (Delta)
    # Fórmula: Delta = b² - 4 * a * c
    delta = b**2 - 4*a*c

    # Mostra o valor encontrado para Delta
    print("\nValor de Delta:", delta)

    # Verifica se Delta é maior que zero
    if delta > 0:

        # Calcula as duas raízes reais distintas
        # math.sqrt(delta) calcula a raiz quadrada de Delta
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        # Exibe o resultado
        print("A equação possui duas raízes reais distintas.")
        print("Primeira raiz (x1):", x1)
        print("Segunda raiz (x2):", x2)

    # Verifica se Delta é igual a zero
    elif delta == 0:

        # Calcula a única raiz real (duas raízes iguais)
        x = -b / (2*a)

        # Exibe o resultado
        print("A equação possui uma raiz real.")
        print("Raiz:", x)

    # Se Delta for menor que zero
    else:

        # Informa que não existem raízes reais
        print("\nA equação não possui raízes reais.")
        print("Possui duas raízes complexas.\n")


# Solicita ao usuário os valores dos coeficientes
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verifica se o valor de a é diferente de zero
# Se a for zero, a equação não será do segundo grau
if a == 0:
    print("Erro! O valor de a deve ser diferente de zero.")

# Se a for diferente de zero, chama a função
else:
    calcular_raizes(a, b, c)

'''Essa questão você deve criar seu próprio módulo, ou seja, a questão deverá ter dois
arquivos, 1 para o módulo e outro para o código principal. Imagine que você trabalhe na parte
de Cibersegurança de uma empresa e precise testar se as senhas criadas pelos usuários estão
no padrão da empresa. O seu módulo deverá ter uma função que verifique as senhas pelos
critérios:
- Pelo menos 8 caracteres;
- Contém pelo menos uma letra maiúscula;
- Contém pelo menos um número;
- Caso os critérios não sejam seguidos, informar ao usuário.
Dica: utilize no seu módulo a biblioteca re'''

# Deixei tudo comentado e salvo neste mesmo arquivo para facilitação da visualização

# ARQUIVO 1: modulo_senha.py
#Este arquivo contém a função responsável pela validação das senhas.

'''# Importa a biblioteca re
import re

# Cria a função para validar a senha
def validar(senha):

    # Verifica se a senha possui 8 ou mais caracteres
    tamanho = len(senha) >= 8

    # Verifica se possui pelo menos uma letra maiúscula
    maiuscula = re.search(r'[A-Z]', senha)

    # Verifica se possui pelo menos um número
    numero = re.search(r'[0-9]', senha)

    # Verifica se todos os critérios foram atendidos
    if tamanho and maiuscula and numero:
        return True

    else:
        print("\nSenha não atende aos requisitos!")

        # Informa qual critério não foi atendido
        if not tamanho:
            print("- A senha precisa ter pelo menos 8 caracteres.")

        if not maiuscula:
            print("- A senha precisa ter uma letra maiúscula.")

        if not numero:
            print("- A senha precisa ter pelo menos um número.")

        return False'''


# ARQUIVO 2: principal.py
# Este arquivo importa e utiliza a função criada no módulo modulo_senha.py.

'''# Importa a função do módulo criado
from modulo_senha import validar

# Solicita a senha ao usuário
senha = input("Digite uma senha: ")

# Chama a função e verifica o resultado
if validar(senha):
    print("\nSenha cadastrada com sucesso!")

else:
    print("\nTente criar outra senha.")'''
