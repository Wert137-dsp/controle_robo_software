import mysql.connector

conexao = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "bd_robo")

cursor = conexao.cursor()

