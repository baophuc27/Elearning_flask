from urllib import parse

# FOR SQL AUTHENTICATION
# params =parse.quote_plus("DRIVER={SQL Server};SERVER=SERVER_NAME;DATABASE=DB;UID=user;PWD=password")

#FOR WINDOWS AUTHENTICATION
params=parse.quote_plus('Driver={SQL Server};Server=DESKTOP-KQ9A20T\TRUCLU;Database=ass2new;Trusted_Connection=yes;')
SQLALCHEMY_DATABASE_URI="mssql+pyodbc:///?odbc_connect=%s" % params
