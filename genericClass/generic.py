import pyodbc


class genericManage:

    def conSQL(server_, database_, username_, password_):
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server_+';DATABASE='+database_+';UID='+username_+';PWD=' + password_)
        return cnxn

    def select(sql, campo):
        return campo
        
