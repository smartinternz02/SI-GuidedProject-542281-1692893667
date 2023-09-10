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
        print("The Role  is : ",  dictionary["ROLE"])
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

try:
    import ibm_db
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bfn16116;PWD=MGhjYY9rDOfBvqko",'','')
    print(conn)
    print("connection successful...")
    insertdb(conn,"Gunabalan","guna@gmail.com",'1234567890','Electrical Machines','50771','faculty','1234567')
    getdetails("guna@gmail.com",'1234567')
    showall()

except:
    print("Error connecting to the database")



