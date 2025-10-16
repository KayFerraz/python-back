# Faça um programa para realizar a busca por uma palavra-chave no
#  conteúdo de um arquivo texto (.cpp, .java,.txt, etc). As informações 
# sobre o nome do arquivo e da palavra a ser procurada serão informadas 
# pelo usuário. Ao final do processamento informe, caso encontre, em quais
#  linhas do arquivo a palavra chave foi encontrada. Na solução crie a função: 
# analisa(linha_arquivo, palavra_chave) que ao ser executada retorne True caso 
# o segundo parâmetro estiver contido no primeiro e False caso contrário

def analisa(linha_arquivo, palavra_chave):
    if palavra_chave in linha_arquivo:
        return True
    return False

with open('novo_arquivo.txt', 'w') as arquivo:
    escrever = input('digite algo:')
    arquivo.write(escrever)
    print('arquivo criado com sucesso!')

with open('novo_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

print('Busca por palavra chave no arquivo')
palavra_chave = input('Digite a palavra chave que deseja buscar:')

with open('novo_arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
        if analisa(linha, palavra_chave):
            print(f'Palavra chave encontrada na linha {i + 1}')