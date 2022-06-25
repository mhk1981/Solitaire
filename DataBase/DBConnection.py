import mysql.connector
from Classes.Player import Player


class DBConnection:
    def __init__(self):
        self.mydb = None
        self.cursor = None
        self.result = None
        self.player = Player()

    # ===========================#
    def connect(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="8288"
        )
        self.cursor = self.mydb.cursor()
        print(self.mydb)

    # ======add new player to db ======#
    def addNewPlayer(self):
        success = False
        sql = "INSERT INTO player(id, userName, email, password, score) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (self.player.get_id(), self.player.get_userName(), self.player.get_email(),
                 self.player.get_password(), self.player.get_score())

        try:
            # Executing the SQL command
            self.cursor.execute(sql, value)
            # Commit changes in the database
            self.mydb.commit()
            success = True

        except mysql.connector.Error as error:
            success = False

        return success

    # ======display one player depend on his password =====
    def displayOnePlayer(self, password):
        success = False
        sql = "SELECT * FROM player WHERE password =" + password

        try:
            # Executing the SQL command
            self.cursor.execute(sql)
            # get the result from DB
            self.result = self.cursor.fetchall()
            success = True

        except mysql.connector.Error as error:
            success = False

        return success

    # =======update player's userName =========
    def updatePlayerUserName(self, newUserName):
        success = False
        sql = "UPDATE player SET userName = " + newUserName

        try:
            # Executing the SQL command
            self.cursor.execute(sql)
            # Commit changes in the database
            self.mydb.commit()
            success = True

        except mysql.connector.Error as error:
            success = False

        return success

    # =======update player's password =========
    def updatePlayerPassword(self, newPassword):
        success = False
        sql = "UPDATE player SET password = " + newPassword

        try:
            # Executing the SQL command
            self.cursor.execute(sql)
            # Commit changes in the database
            self.mydb.commit()
            success = True

        except mysql.connector.Error as error:
            success = False

        return success

    # =======update player's email =========
    def updatePlayerEmail(self, newEmail):
        success = False
        sql = "UPDATE player SET email = " + newEmail

        try:
            # Executing the SQL command
            self.cursor.execute(sql)
            # Commit changes in the database
            self.mydb.commit()
            success = True

        except mysql.connector.Error as error:
            success = False

        return success

    # =======update player's score =========
    def updatePlayerScore(self, newScore):
        success = False
        sql = "UPDATE player SET password = " + newScore

        try:
            # Executing the SQL command
            self.cursor.execute(sql)
            # Commit changes in the database
            self.mydb.commit()
            success = True

        except mysql.connector.Error as error:
            success = False

        return success

    # =============delete one player ==============
    def deletePlayer(self, password):
        success = False
        sql = "DELETE FROM player WHERE password = " + password

        try:
            # Executing the SQL command
            self.cursor.execute(sql)
            # Commit changes in the database
            self.mydb.commit()
            success = True

        except mysql.connector.Error as error:
            success = False

        return success

    # ========close Connection ================
    def closeConnection(self):
        self.cursor.close()
        self.mydb.close()
