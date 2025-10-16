# Desenvolva um programa em Python que faz a leitura de um número inteiro e 
# decomponha os dígitos desse número em uma lista, onde cada dígito ocupará
# uma posição do vetor. Por exemplo, se o usuário digitar o número 1300, 
# deverá retornar a lista [1,3,0,0]

def dec_Num(num):
    list_num= []
    while num>0: 
        digito = num % 10
        list_num.append(digito)
        num = num // 10
    return list_num[::-1]

num = int(input('Digite um número inteiro: '))
print(dec_Num(num))