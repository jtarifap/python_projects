from genericClass import generic
from tkinter import *

server = 'SERVINTRA01\SQLINTRA'
database = 'VVTecnics_TEST'
username = 'sa'
password = '********'

""" server = 'VICENSSBONE2\VICENSVIVES'
database = 'VVEDITORIAL_JORGE'
username = 'sa'
password = '********' """


gen = generic
cnxn = gen.genericManage.conSQL(server, database, username, password)
cursor = cnxn.cursor()
fecha = ""
# Sample select query
"""  sql = "SELECT * from facturas" """
sql = "select  top 1 * from oinv order by DocEntry desc"
cursor.execute(sql)


row = cursor.fetchone()
contCampos = row.cursor_description.count
while row:
    va1 = row[0]
    va2 = row[1]
    va3 = row[2]
    va4 = row[3]
    print(str(va1) + ' --- ' + str(va2) +
          ' --- ' + str(va3) + ' --- ' + str(va4))
    # lab = Label(root, text=str(va1) + ' --- ' + str(va2) +
    #            ' --- ' + str(va3) + ' --- ' + str(va4))
    # lab.pack()
    row = cursor.fetchone()
