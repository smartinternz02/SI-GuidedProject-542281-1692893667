from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/faculty')
def faculty():
    return render_template("faculty.html")

@app.route('/submission')
def submission():
    return render_template("submission.html")

@app.route('/login1', methods = ['POST',"GET"])
def login1():
    NAME = request.form['NAME']
    EMAIL = request.form['EMAIL']
    if NAME == "Guna" and EMAIL == "gunabalan.r@vit.ac.in":
        return " Welcome to portal"
    else:
        return render_template("register.html")

@app.route('/register1', methods = ['POST','GET'])
def register1():
    NAME = request.form['NAME']
    EMAIL = request.form['EMAIL']
    PASSWORD = request.form['PASSWORD']
    return render_template("login.html")
@app.route('/faculty1', methods = ['POST','GET'])
def faculty1():
        NAME = request.form['NAME']
        EMPID = request.form['EMPID']
        EMAIL = request.form['EMAIL']
        DESIGNATION = request.form['DESIGNATION']
        DEPARTMENT = request.form['DEPARTMENT']
        PASSWORD = request.form['PASSWORD']
        return render_template("login.html")
    
@app.route('/submission1', methods = ['POST','GET'])
def submission1():
            NAME = request.form['NAME']
            REGNO = request.form['REGNO']
            TITLE = request.form['TITLE']
            ASSESSMENT = request.form['ASSESSMENT']
            UPLOAD = request.form['UPLOAD']
            return render_template("login.html")

if __name__ == "__main__":
    app.run(debug = True,port = 5000,host ='0.0.0.0')