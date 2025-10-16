# Escreva um programa em Python que solicita ao 
# usuário uma medida em metros e então a converta 
# e exiba em milhas, pés e polegadas.
#      	pes = metros x 3,2808
#      	polegadas = metros x 39,37
metros= float(input("Informe a medida em metros:"))  
pes = metros*3.2808
polegadas = metros * 39.37

print(f'VALOR EM METROS: {metros:.2f} ')
print(f'VALOR EM PÉS: {pes:.2f}')
print(f'VALOR EM POLEGADAS:{polegadas:.2f}')

