from flask import *
import os
import socket
import pyodbc
template_dir=os.path.abspath("/templates")

app=Flask(__name__)
app.secret_key="alo"
app.config.from_pyfile('config.cfg')

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run()
    
    