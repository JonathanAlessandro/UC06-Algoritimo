import pymysql as pysql
# cria a conexão com o banco de dados

conexao = pysql.connect(
    host="localhost",                     # endereço de servidor (local = 'localhost")
    user="root",                       # usuario do mysql
    password="" ,                       # senha do mysql
    database="bd_livrariaonline" ,       # banco que voce ja criou
    port=3306                         # porta padrão do mysql    
)

# cria cursor - versão dicionario (retorna {"coluna":"valor"}) // e uma boa pratica pois retorna em formato de dicionario
cursor = conexao.cursor(pysql.cursors.DictCursor)

# --- buscar todos os registros ------------
#todos os registros são atribuidos ao cursor
#o ".execute()" serve para executar comandos sql 
cursor.execute("select * FROM clientes")
#agora "todos" recebe os dados da data base e o .fetchall() transforma em dicionario
todos = cursor.fetchall()

# for cliente in todos:
#     print(cliente["nome"],"-", cliente["email"],"-", cliente["telefone"])

# buscando 1 unico registro por ID

cursor.execute("select * from clientes where id_cliente = 1")

cliente = cursor.fetchone()

print(cliente) #{'id':1,'nome','maria','email':'.....'}

#filtro dinamico (SEGURO)
#o "%" ao final continua a busca por outros nomes iguais
nome_busca = "Ana%"

#esse "%s" funciona como o "f" no print espera uma variavel no lugar nesse exemplo uso a variavel "nome_busca" retorna como "Tuplas"
cursor.execute("select * from clientes where nome like %s",(nome_busca),)

#agora os dados do ultimo execute são atribuidos ao resultado
resultado = cursor.fetchall()

print(resultado)