# . Crie a função inserir que recebe como parâmetros um
#  dicionário com os dados de um 
# idosos/colaboradores e usando o
#  comando SQL INSERT, armazene os dados na tabela

import sqlite3

pessoas = {
    1: {"id": 1, "cpf": "12345678900", "nome": "Ana Clara", "voluntario": "SIM"},
    2: {"id": 2, "cpf": "98765432100", "nome": "Bruno Souza", "voluntario": "NAO"},
    3: {"id": 3, "cpf": "45678912300", "nome": "Carla Mendes", "voluntario": "SIM"}
}
try:
    iniciar = sqlite3.connect("voluntarios.db")
    cur = iniciar.cursor()
    for pessoa in pessoas.values():
        cur.execute("""
        INSERT INTO colaborador (id, cpf, nome, voluntario)
        VALUES (?, ?, ?, ?)
        """, (pessoa["id"], pessoa["cpf"], pessoa["nome"], pessoa["voluntario"]))

    iniciar.commit()
    cur.execute("SELECT nome FROM colaborador")
    res = cur.fetchall()
    print(res)

    cur.close()
    iniciar.close()

except sqlite3.Error as error:
    print("Erro:", error)