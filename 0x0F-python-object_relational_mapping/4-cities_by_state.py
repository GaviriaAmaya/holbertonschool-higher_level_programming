#!/usr/bin/python3
"Prints all the cities according to the state id order"
import sys
import MySQLdb


if __name__ == "__main__":

    if (len(sys.argv) == 4):
        dtb = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                              passwd=sys.argv[2], database=sys.argv[3])
        cur = dtb.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM states\
                    INNER JOIN cities ON states.id = cities.state_id\
                    ORDER BY cities.id ASC")

        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

        cur.close()
        dtb.close()
