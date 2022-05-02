import pyodbc
from multiprocessing import Manager
from multiprocessing.spawn import import_main_path
from tkinter import *

from genericClass import generic

"""
server = 'SERVINTRA01\SQLINTRA'
database = 'VVTecnics_TEST'
username = 'sa'
password = 'vvp.20'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server +
                      ';DATABASE='+database+';UID='+username+';PWD=' + password)
"""""
server = 'SERVINTRA01\SQLINTRA'
database = 'VVTecnics_TEST'
username = 'sa'
password = 'vvp.20'

gen = generic
#gen.ConSQL
"""def ConSQL(server, database, username, password):
    # Some other example server values are
    # server = 'localhost\sqlexpress' # for a named instance
    # server = 'myserver,port' # to specify an alternate port

    return pyodbc.connect('DRIVER={SQL Server};SERVER='+server +
                          ';DATABASE='+database+';UID='+username+';PWD=' + password)
"""
#gen.genericManage.conSQL()
def testSelect():
    cnxn = gen.genericManage.conSQL(server, database, username, password)
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
        print(str(va1) + ' --- ' + str(va2) +
              ' --- ' + str(va3) + ' --- ' + str(va4))
        lab = Label(root, text=str(va1) + ' --- ' + str(va2) +
                    ' --- ' + str(va3) + ' --- ' + str(va4))
        lab.pack()
        row = cursor.fetchone()


def calcular(importe, descuento):
    # return importe - (importe * descuento / 100)
    lab = Label(root, text=importe - (importe * descuento / 100))
    lab.pack()


datos = {"descuento": 10, "importe": 1500}


def Call():  # Definimos la funcion
    lab = Label(root, text='Usted presiononel boton')
    lab.pack()
    boton['bg'] = 'blue'  # Al presionar queda azul
    boton['fg'] = 'white'  # Si pasamos el Mouse queda blanco


# print calcular(234, 10)
root = Tk()  # Ventana de fondo
root.geometry('800x600+300+70')  # Geometría de la ventana

boton = Button(root, text='Presionar', command=testSelect)
boton.pack()
root.mainloop()
