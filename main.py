from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb 
import bcrypt 
app = Flask(__name__)
 
app.secret_key = "caircocoders-ednalan-2020"
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'admin'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)
 
@app.route('/')
def home():
    return render_template("home.html")
 
@app.route('/register', methods=["GET", "POST"]) 
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
 
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",(name,email,hash_password,))
        mysql.connection.commit()
        session['name'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('login'))
 
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
 
        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users WHERE email=%s",(email,))
        user = curl.fetchone()
        curl.close()
 
        if len(user) > 0:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return redirect("index")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("login.html")
@app.route('/index',methods=["GET","POST"])
def index():
    if request.method=='GET':
        cur2=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        s="SELECT * FROM employee"
        cur2.execute(s)
        output_data=cur2.fetchall()
        cur2.close()
        return render_template("index.html", output_data=output_data, s=s)
    else:
        name=request.form['name']
        desig=request.form['designation']
        salary=request.form['salary']
@app.route('/create',methods=["GET","POST"])
def create():
        if request.method == 'GET':
            return render_template("create.html")
        else:
            name = request.form['name']
            designation = request.form['designation']
            salary = request.form['salary']
 
            cur3 = mysql.connection.cursor()
            cur3.execute("INSERT INTO employee (name, designation, salary) VALUES (%s,%s,%s)"(name,designation,salary))
            mysql.connection.commit()
            session['name'] = request.form['name']
            session['designation'] = request.form['designation']
            session['salary'] = request.form['salary']
            return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return render_template("home.html")
     
if __name__ == '__main__':
    app.run(debug=True)