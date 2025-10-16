# 2 Escreva um programa que peça um número
#  inteiro e mostre todos os seus divisores.
print("Me informe um número e eu mostro os divisores")
num = int(input("Informe um número:"))
cont = 1
lista=[]

for cont in range(1,num+1):
    calc = num % cont
    if calc == 0:
        lista.append(cont)
    
print(lista)
