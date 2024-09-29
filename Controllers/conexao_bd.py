import mysql.connector

conexao = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bd_robo")

cursor = conexao.cursor()

cursor.execute("select * from usuario")

result = cursor.fetchall()

print(result)
print("123")