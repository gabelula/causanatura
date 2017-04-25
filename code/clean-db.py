#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import psycopg2

def main():
    conn = psycopg2.connect("dbname=causa user=Gabriela")
    cur = conn.cursor()
    cur.execute("SELECT * FROM beneficiarios;")

    for row in cur.fetchall():
        print(row)

if __name__ == "__main__":
    main()
