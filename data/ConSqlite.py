import sqlite3


class ConSqlite():

    @staticmethod
    def getConexao():

        dbName = 'data/RegistroDB'
        con = sqlite3.connect(dbName +'.sqlite')
        
        return con
