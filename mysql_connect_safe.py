import mysql.connector
from password_utils import get_decrypted_password

def connect_to_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="tamil"
    )
    print("Connected to MySQL database successfully!")
    print(get_decrypted_password())
    conn.close()

if __name__ == "__main__":
    connect_to_mysql()