#!/usr/bin/python3
"Lists All states starting with N"
import sys
import MySQLdb


if __name__ == "__main__":

    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                          passwd=sys.argv[2], database=sys.argv[3])
    cur = dtb.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER\
                BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()

    print(query_rows)

    cur.close()
    dtb.close()
