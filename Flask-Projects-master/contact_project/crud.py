from flask import *
import datetime
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");

@app.route("/add")
def add():   
    return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
    msg = ""
    if request.method == "POST":
        try:
            First_Name = request.form["firstname"]
            Last_Name = request.form["lastname"]
            Mobile_Number = request.form["mnumber"]
            Office_Number = request.form["onumber"]
            E_mail = request.form["mail"]
            Address = request.form["address"]
            with sqlite3.connect("C:\\Users\\Praveen Kumar\\Downloads\\Flask-Projects-master\\contact_project\\contact.db") as connection:
                cursor = connection.cursor()   
                cursor.execute("""insert into dbservice (FirstName,LastName,MobileNumber,OfficeNumber,mailid,address)
                values(?,?,?,?,?,?);""",(First_Name,Last_Name,Mobile_Number,Office_Number,E_mail,Address))
                connection.commit()
                msg = "Contact successfully Added"   
        except:
            connection.rollback()
            msg = "Can't Add Details Into Contact List Check The Input Data's"
        finally:
            return render_template("success.html",message = msg)
            connection.close()

@app.route("/view")
def view():
    ip = request.environ.get('HTTP_X_REAL_IP',request.remote_addr)
    http = request.url
    time = datetime.datetime.now()
    count = 1
    msg = ""
    try:
            nip = ip
            nhttp = http
            ntime = time
            ncount = count 
            nSno = "1"
            with sqlite3.connect("C:\\Users\\Praveen Kumar\\Downloads\\Flask-Projects-master\\contact_project\\contact.db") as connection:
                cursor = connection.cursor()   
                cursor.execute("""insert into dbservice (ip,http,time,count,Sno)
                values(?,?,?,?,?,?);""",(nip,nhttp,ntime,ncount,nSno))
                connection.commit()
                msg = "Contact successfully Added"   
        except:
            connection.rollback()
            msg = "Can't Add Details Into Contact List Check The Input Data's"
        finally:
            return render_template("success.html",message = msg)
            connection.close()
        
    with sqlite3.connect("C:\\Users\\Praveen Kumar\\Downloads\\Flask-Projects-master\\contact_project\\contact.db") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        #str = "select * from dbservice where ip=" + ip
        cursor.execute("select * from dbservice ")
        data = cursor.fetchall()       
        return render_template("view.html",rows = data)
        
        
        

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deleterecord",methods = ["POST"])   
def deleterecord():
    id = request.form["sno"]
    with sqlite3.connect("C:\\Users\\Praveen Kumar\\Downloads\\Flask-Projects-master\\contact_project\\contact.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from dbservice where Sno= ?",id)
            msg = "Contact successfully Deleted"   
        except:
            msg = "Can't Be Deleted"
        finally:
            return render_template("delete_record.html",msg = msg)

if __name__ == "__main__":
    app.run(debug = True)  