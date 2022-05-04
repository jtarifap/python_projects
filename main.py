#prueba de acceso SQL Server
from unittest.util import sorted_list_difference
import pyodbc
""" from multiprocessing import Manager
from multiprocessing.spawn import import_main_path """
from tkinter import *

from genericClass import generic
from dbaccess import db

bd = db()
server = bd.server
database = bd.dbname
username = bd.us
password = bd.passw
print(bd)
gen = generic.genericManage

 
def testSelect():
    cnxn = gen.conSQL(server, database, username, password)

   # cnxn = ConSQL(server, database, username, password)
    cursor = cnxn.cursor()
    fecha = ""
    # Sample select query
    cursor.execute("SELECT * from facturas")
    row = cursor.fetchone()
    while row:
        va1 = row[0]
        va2 = row[1]
        va3 = row[2]
        va4 = row[3]
        #print(str(va1))

        print(str(va1) + ' --- ' + str(va2) +
              ' --- ' + str(va3) + ' --- ' + str(va4))
        row = cursor.fetchone()

print(testSelect())
