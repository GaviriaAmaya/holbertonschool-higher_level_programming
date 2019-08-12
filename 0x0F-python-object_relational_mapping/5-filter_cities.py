#!/usr/bin/python3
"Prints all the cities according to the state id order"
import sys
import MySQLdb


if __name__ == "__main__":

    if (len(sys.argv) == 5):
        dtb = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                              passwd=sys.argv[2], database=sys.argv[3])
        cur = dtb.cursor()
        cur.execute("SELECT cities.name FROM states\
                    INNER JOIN cities ON states.id = cities.state_id\
                    WHERE states.name = '{}'\
                    ORDER BY cities.id ASC".format(sys.argv[4].split('\'')[0]
                                                   .split(';')[0]))

        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

        cur.close()
        dtb.close()
