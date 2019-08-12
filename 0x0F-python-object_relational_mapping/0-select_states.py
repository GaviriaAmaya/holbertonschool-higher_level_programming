#!/usr/bin/python3
#Lists all the atates from the database
import sys
import MySQLdb


if __name__ == "__main__":

    if (len(sys.argv == 4)):
        dtb = MySQLdb.connect(host="localhost", user=sys.argv[1], port="3306",
                              passwd=sys.argv[2], database=sys.argv[3])
    cur = dtb.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    dtb.close()
