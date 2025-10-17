# try: 
#     arq = open("C:..\\Dev-Cpp\\news.txt","r")
#     linha = arq.readline()
#     print(linha)
#     arq.close()
    
# except:
#     print("ERRO DE ABERTURA")

    
# try: 
#     arq = open("C:..\\Dev-Cpp\\news.txt","r")
#     while True:
#         linha = arq.readline()
#         if linha == "":
#             break
#         print(linha,end="") # para nao pular linha 
        
#     arq.close()
# except:
#     print("ERRO DE ABERTURA")

# try: 
#     arq = open("C:..\\Dev-Cpp\\news.txt","r")
#     arquivo2 = open("D:/novo.txt","w")
#     while True:
#         linha = arq.readline()
        
#         if linha == "":
#             break
#         arquivo2.write(linha.upper()+"\n")    
#         print(linha,end="") # para nao pular linha 
#     arquivo2.close()
#     arq.close()
    
# except:
#     print("ERRO DE ABERTURA")

try: 
    arquivo = open("textoNovo.txt","+a")
    # a+ permite que grave no final do arquivo,pulando linha
    frase = input("Informe seu texto: ")
    arquivo.write(frase+"\n")
    # arquivo.seek(2)   #final do arq
   
    arquivo.close()
    
except:
    print("ERRO DE ABERTURA")
   

