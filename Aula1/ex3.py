#AULA DIA 10/10 - PRIMEIRA AULA
# Atribuição múltipla:
# 	r=g=b=10
# Atribuição múltipla distinta:
# 	r,g,b = 200,50,30
# Removendo uma variável:
# 	del r

#----------- 3 Jogo  da  Adivinhação
#   Desenvolva  um  programa  em  Python que 
#  simule  um  jogo  de  adivinhação.  
# Primeiramente,  o  programa  deverá  
# sortear  um  número  entre  0  e  100.  
# Após  o  sorteio,  inicia-se  o  jogo  e 
#  o jogador deverá tentar adivinhar o número
#  sorteado. A cada tentativa, o jogo deverá 
# informar se o “chute” do jogador foi maior ou 
# menor do que o número a ser adivinhado. 
# O jogo termina após vinte tentativas erradas
#  ou  quando  o  jogador  acertar  o  número  
# sorteado  e,  nesse  caso,  informe  a  
# quantidades  de  tentativas  que  foram 
#  necessárias.   

from random import randint
num = randint(0,100)
listaTent=[]
print(num)
contVida = 0
# JOGO ENCERRA COM 20 TENTATIVAS
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO")
print("/!\ LEMBRANDO QUE: VOCÊ ENCERRA COM 20 VIDAS")
print("VOCE DEVERÁ ADIVINHAR O NUMERO SORTEADO. BOA SORTE.")

adivinha = -1  

while adivinha != num and contVida < 20:
    try:
        adivinha = int(input("Informe o número: "))
    except ValueError:
        print("Digite apenas números inteiros!\n")
        continue

    contVida += 1
    listaTent.append(adivinha)

    if adivinha > num:
        print("O número digitado é MENOR  do que o sorteado.\n")
    elif adivinha < num:
        print("O número digitado é MAIOR do que o sorteado.\n")

if adivinha == num:
    print(f"\n PARABÉNS, VOCÊ ACERTOU O NÚMERO {num}!")
    print(f"Tentativas: {contVida}")
    print(f"Chutes: {listaTent}")
else:
    print("\n ACABARAM AS VIDAS!")
    print("-----")
    print("|o o|")
    print("| X |")
    print("-----")
    print(f"O número sorteado era {num}.")
    print(f"Tentativas: {listaTent}")
        
