import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0509juan'
)

print("Conexão estabelecida")
mydb.close()