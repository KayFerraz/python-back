#  Utilizando o DB Browser, crie uma base de dados com uma 
# tabela para armazenar os dados 
# dos colaboradores ou dos idosos seu projeto da disciplina.
#  Não esqueça de considerar que 
# cada idoso/colaborador tem um ID

import sqlite3
try:
    iniciar = sqlite3.connect("voluntarios.db")
    cur = iniciar.cursor()
    nome='Maria Antonia'
    voluntario = 'NAO'
    sql=f"INSERT INTO colaborador VALUES (589696564452,'LUA', 'SIM')"
    cur.execute(sql)
    iniciar.commit()
    sql="SELECT nome FROM colaborador"
    cur.execute(sql)
    res=cur.fetchall()
    print(res)
    cur.close()
    iniciar.close()
except sqlite3.Error as error:
    print(error)