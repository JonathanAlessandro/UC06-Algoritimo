import pymysql as pysql

conexao = pysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bd_livrariaonline",
    port=3306
)

cursor = conexao.cursor(pysql.cursors.DictCursor)

try:
    # #comando para inserir dados de um novo registro
    # sql_insert = "insert into clientes (nome,email) values (%s,%s)"
    
    # #antes de rodar lembrar de comentar ess parte
    # cursor.execute(sql_insert,("Ala Lima","bnasf@gmail.com"))
    # conexao.commit() # confirma o insert e a ação de realizar o insert como no git
    # print("Inserido com sucesso! ID: ", cursor.lastrowid)
    # #retorna o id que foi criado
    
    # #update
    # sql_update = "update clientes set email = %s where id_cliente= %s"
    # cursor.execute(sql_update,("novo@email.com",1))
    # conexao.commit()# confirma o update
    # print ("Linhas afetadas: ",cursor.rowcount)
    
    #DELETA DO BANCO
    #não vai deletar pois o banco está com o relacionamento das fk e não permiti a exlcusão
    
    cursor.execute("delete from clientes where id_cliente= %s",(5,))
    conexao.commit()# confirma o update
    
    
except Exception as erro:
    conexao.rollback()
    print("Erro! Operação revertida: ",erro)

# e executando independente de erro ou ter ocorrido tudo normalmente
finally:
    #fecha a conexão com cursor
    cursor.close()
    #fecha a conexão com o banco
    conexao.close() #boa pratica para não deixar possiveis falhas


print(2**128)