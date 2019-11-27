from flask import *
import os
import socket
template_dir=os.path.abspath("/templates")
app=Flask(__name__)
app.secret_key="alo"

@app.route("/")
def index():
    return render_template("index.html")
    
if __name__ == "__main__":
    app.run()
    
    