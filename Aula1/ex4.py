#4) Embaralhar as palavras é um tipo de quebra-cabeças que é popular com crianças.
#  As letras em cada palavra são rearranjadas em uma ordem qualquer e a pessoa 
# que está usando o quebra-cabeças tem que descobrir qual era a palavra original. 
# Palavras com três e quatro letras são fáceis, mas quanto mais letras são adicionadas,o
#  número de combinações possíveis cresce rapidamente, deixando o quebra-cabeças mais 
# desafiador. Crie um programa em Python que ao ler uma palavra qualquer a exiba de 
# forma embaralhada
 #passo 1: lista de palavras
#passo 2: embaralhar
#if else acerto 
import random


lista_de_palavras = [ "maçã", "banana", "laranja", "uva", "morango",
    "abacaxi", "melancia", "pera", "manga", "kiwi",
    "mamão", "cereja", "ameixa", "goiaba", "limão",
    "caqui", "figo", "jabuticaba", "pêssego", "framboesa"]
palavra_original = random.choice(lista_de_palavras) #embaralhando palavra

palavra_aleatoria = list(palavra_original)  #transformando em lista para radom
random.shuffle(palavra_aleatoria) #embaralhando a lpalavra escolhida
palavra_embaralhada = ''.join(palavra_aleatoria) #transformando em string
print("Palavra embaralhada: ", palavra_embaralhada)

letra = input("Digite uma palavra: ").lower()

while letra != palavra_original:
        print("Você errou, tente novamente!")
        letra = input("Digite uma palavra: ").lower()

print("Parabéns, você acertou!")
print("A palavra era: ", palavra_original)

