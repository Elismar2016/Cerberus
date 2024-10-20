import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="dev@2024",
        db="cerberus_db"
    )
    print("Conectado com sucesso!")
except MySQLdb.Error as e:
    print(f"Erro na conexão: {e}")
