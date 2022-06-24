import mysql.connector


class DBConnection:
    def __init__(self):
        self.mydb = None

    # ===========================#
    def connect(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="8288"
        )
        print(self.mydb)
