# Crie a função apagar que ao receber o ID do idoso/colaborador, faça a deleção do mesmo, 
# use o comando SQL DELETE.

import sqlite3

try: 
    sqlite_con = sqlite3.connect("voluntarios.db")
    cursor = sqlite_con.cursor()

except sqlite3.Error as error:
    print("Erro:", error)