from flask import Flask, render_template,request
import sqlite3

data = sqlite3.connect("studentdata.db",check_same_thread=False)
table = data.execute("select name from sqlite_master where type='table' and name='student' ").fetchall()
if table!=[]:
    print("Table already exists")

else:
    data.execute('''create table student(
                                        id integer primary key autoincrement,
                                        Name text,
                                        branch text,
                                        rollno integer,
                                        admno integer,
                                        DOB text,
                                        pass text,
                                        semester text
                                        );''')
    print("Table created")

app = Flask(__name__)

@app.route('/')
def Student_Login_page():
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def Student_Registration_page():
    if request.method == "POST":
        getName = request.form["name"]
        getBranch = request.form["branch"]
        getRollno = request.form["rollno"]
        getAdmno = request.form["admissionnumber"]
        getDOB = request.form["DOB"]
        getSem = request.form["semester"]
        getPass = request.form["password"]
        getConpass = request.form["confirmpassword"]
        print(getName)
        print(getBranch)
        print(getRollno)
        print(getAdmno)
        print(getDOB)
        print(getSem)
        print(getPass)
        print(getConpass)
        try:
            query = "insert into student(Name,branch,rollno,admno,DOB,pass,semester)\
                     values('"+getName+"','"+getBranch+"',"+getRollno+","+getAdmno+",'"+getDOB+"','"+getSem+"','"+getPass+"')"
            data.execute(query)
            print(query)
            data.commit()
            data.close()
            print("Inserted successfully")
        except Exception as err:
            print("error occured",err)



    return render_template("register.html")

@app.route('/search')
def Student_Search_page():
    return render_template("search.html")

@app.route('/delete')
def Student_Deletion_page():
    return render_template("delete.html")


if __name__== "__main__":
    app.run()
