from flask import Flask
from flask import Markup
#from flask import Flask - Already imported on above
from flask_mysqldb import MySQL
#from flask.ext.mysql import MySQL - dont need this - already imported above
from flask import render_template
import Algorithmia
#import MySQLdb - NO such module


app = Flask(__name__)
#app.config['MYSQL_HOST'] = 'C:\Program Files\MySQL\MySQL Server 5.7\bin'
app.config['MYSQL_HOST'] = 'localhost' # host requires the network address of mysql
app.config['MYSQL_USER'] = 'root@localhost'
app.config['MYSQL_PASSWORD'] ='root'
#app.config['MYSQL_DB'] = 'EmpData.sql'
app.config['MYSQL_DB'] = 'anshula_charting' # Needs a DB name. Use this command to create: create database anshula_charting;
mysql = MySQL(app)

@app.route("/")

def chart():
    labels = ["January","February","March","POOP","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', values=values, labels=labels)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)


