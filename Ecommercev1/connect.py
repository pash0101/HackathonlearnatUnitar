import MySQLdb



def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "root",
                           db = "indus")
    c = conn.cursor()

    return c, conn

test = connection()