from flask import Flask
from flask import Markup
from flask import Flask
from flask_mysqldb import MySQL
from flask.ext.mysql import MySQL
from flask import render_template
import Algorithmia
import MySQLdb


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'C:\Program Files\MySQL\MySQL Server 5.7\bin'
app.config['MYSQL_USER'] = 'root@localhost'
app.config['MYSQL_PASSWORD'] ='root'
app.config['MYSQL_DB'] = 'EmpData.sql'
mysql = MySQL(app)

@app.route("/")

def chart():
    labels = ["January","February","March","POOP","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)


