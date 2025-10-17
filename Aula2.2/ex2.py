#Crie manualmente um arquivo texto com 10 
# perguntas sobre a linguagem Python, onde 
# cada pergunta deve ocupar uma linha do arquivo. 
# Agora desenvolva um programa que faça individualmente 
# as 10 perguntas para o usuário. As respostas do 
# usuário devem ser armazenadas em um outro arquivo,
#  de forma que cada uma delas ocupe uma linha do 
# arquivo e tenha o seguinte formato: número da
# pergunta : resposta do usuário : tempo em segundos que o usuário demorou para responder a pergunta.  Pesquise por classes em Python que permitam capturar o tempo, uma delas é a classe datetime, mas existem outras.
# que o usuário demorou para responder
# a pergunta.  Pesquise por classes em Python que
#  permitam capturar o tempo, uma delas é a classe 
# datetime, mas existem outras.
import datetime
import time


tempo_inicial = datetime.datetime.now()
tempo_final = datetime.datetime.now()
tempo_total = tempo_final - tempo_inicial


with open('arquivo_kay.txt', 'w') as arquivo:
    escrever = input('digite algo:')
    
    arquivo.write(escrever)
    print('arquivo criado com sucesso!')

with open('arquivo_kay.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

def fazer_perguntas(perguntas):
    
    return arquivo
aa
print(f'Tempo total para responder as perguntas: {tempo_total}')
for i in range(10):
        linha = input(f"{i+1}. {perguntas[i]}")
        input("1. O que é Python?")
        arquivo.write(linha + '\n')
        input("2. Quais são os tipos de dados básicos em Python?")
        arquivo.write(linha + '\n')
        input("3. O que são listas em Python?")
        arquivo.write(linha + '\n')
        input("4. Como você define uma função em Python?")
        arquivo.write(linha + '\n')
        input("5. O que é um dicionário em Python?")
        arquivo.write(linha + '\n')
        input("6. Como você faz um loop em Python?")
        arquivo.write(linha + '\n')
        input("7. O que são classes em Python?")
        arquivo.write(linha + '\n') 
        input("8. Como você trata exceções em Python?")
        arquivo.write(linha + '\n') 
        input("9. O que é uma compreensão de lista?")
        arquivo.write(linha + '\n')
        input("10. Como você importa módulos em Python?")
        arquivo.write(linha + '\n')