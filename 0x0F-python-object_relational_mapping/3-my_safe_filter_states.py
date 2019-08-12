#!/usr/bin/python3
"Safer from injections"
import sys
import MySQLdb


if __name__ == "__main__":

    dtb = MySQLdb.connect(host="localhost", user='%s' % sys.argv[1], port=3306,
                          passwd='%s' % sys.argv[2],
                          database='%s' % sys.argv[3])
    cur = dtb.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '%s' ORDER\
                BY id ASC" % sys.argv[4])
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    dtb.close()
