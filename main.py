#prueba de acceso SQL Server
import pyodbc
""" from multiprocessing import Manager
from multiprocessing.spawn import import_main_path """
from tkinter import *

from genericClass import generic
from dbaccess import db

"""
server = 'SERVINTRA01\SQLINTRA'
database = 'VVTecnics_TEST'
username = 'sa'
password = '*****'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server +
                      ';DATABASE='+database+';UID='+username+';PWD=' + password)
"""""
#username = 'sa'
#password = '***'
server = db.server
database = db.dbname
username = db.us
password = db.passw

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

testSelect()