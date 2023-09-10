from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from ASSIGNMENT"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ",  dictionary["CONTACT"])
        print("The Course is : ",  dictionary["COURSE"])
        print("The RegNo is : ",  dictionary["REGNO"])
        print("The Role is : ",  dictionary["ROLE"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from ASSIGNMENT where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ", dictionary["CONTACT"])
        print("The Course is : ", dictionary["COURSE"])
        print("The RegNo is : ", dictionary["REGNO"])
        print("The Role is : ", dictionary["ROLE"])
        print("The Password is : ", dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,name,email,contact,course,regno,role,password):
    sql= "INSERT into ASSIGNMENT VALUES('{}','{}','{}','{}','{}','{}','{}')".format(name,email,contact,course,regno,role,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bfn16116;PWD=MGhjYY9rDOfBvqko",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['mobile']
        course = request.form['course']
        register = request.form['regno']
        role = request.form['role']
        if role =="0":
            role = "Faculty"
        else:
            role = "Student"
        password = request.form['pwd']
        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,name,email,contact,course,register,role,password)
        return render_template('login.html')
        

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pwd']
        sql= "select * from ASSIGNMENT where email='{}' and password='{}'".format(email,password)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["EMAIL"]
            return render_template('userprofile.html',name=userdetails["NAME"],email= userdetails["EMAIL"],contact= userdetails["CONTACT"],course=userdetails["COURSE"],register=userdetails["REGNO"],assignment=userdetails["ROLE"],password=userdetails["PASSWORD"])
        else:
            msg = "Incorrect Email id or Password"
            return render_template("login.html", msg=msg)
    return render_template('login.html')


if __name__ =='__main__':
    app.run( debug = True)
