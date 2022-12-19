from os import getenv
import pymssql

class SQLConnect :

    def conDB() :
        server ="192.168.1.40"
        user = "kasin"
        password = "$iN282918598"
        conn = pymssql.connect(server, user, password, "KIN")

        return conn
