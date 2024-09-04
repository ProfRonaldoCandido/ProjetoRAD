'''
Aula05_exemplo01.py
'''
#biblioteca
import sqlite3 as conector #apelido
def criar_banco():
    #mensagem
    print('Abrindo uma conexão de BD')
    #abertura da conexão
    conexao = conector.connect('meu_banco.db')
    #aquisição de um cursor
    cursor = conexao.cursor()
    #execução de comandos SQL
    sql = "CREATE TABLE cadastro(id INTEGER, nome TEXT);"
    cursor.execute(sql)
    cursor.fetchall()
    #efetivação do comando
    conexao.commit()
    #fechamento das conexões
    cursor.close()
    conexao.close()
    #encerrando
    print('Encerrando a conexão')
try:
    criar_banco()
except conector.OperationalError:
    print("Banco de dados com problemas...")
