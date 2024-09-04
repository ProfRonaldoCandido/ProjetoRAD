'''
Aula05_exemplo02.py
'''
# -*- coding: utf-8 -*-
import sqlite3
# Cria uma conexão e um cursor
con = sqlite3.connect('emails.db')
cur = con.cursor()
# Cria uma tabela
sql = 'create table if not exists emails'\
 '(id integer primary key, '\
 'nome varchar(100), '\
 'email varchar(100))'
cur.execute(sql)
# sentença SQL para inserir registros
sql = 'insert into emails values (null, ?, ?)'
# Dados
recset = [('jane doe', 'jane@nowhere.org'),
 ('rock', 'rock@hardplace.com')]
# Insere os registros
for rec in recset:
    cur.execute(sql, rec)
# Confirma a transação
con.commit()
# Seleciona todos os registros
cur.execute('select * from emails')
# Recupera os resultados
recset = cur.fetchall()
# Mostra
for rec in recset:
    print ('%d: %s(%s)' % rec)
# Fecha a conexão
con.close()
