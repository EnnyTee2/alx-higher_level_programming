#!/usr/bin/python3

import MySQLdb as mdb
import sys

try:
    # We connect to a database and create an
    # instance of it to be used in our code
    db_con = mdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db='hbtn_0e_0_usa',
        port=3306)

    curs = db_con.cursor()  # cursor object for transversing the database
    curs.execute("SELECT * FROM states")  # executing an SQL statement

    # storing the SQL query results (rows extracted from selected table)
    record = curs.fetchall()

    for row in record:
        print(row)

except mdb.Error as e:
    print(f"Error {e.args[0]}: {e.args[1]}")
    sys.exit(1)  # exit with standard error

finally:
    if db_con:
        db_con.close()  # close db connection if it is still open
