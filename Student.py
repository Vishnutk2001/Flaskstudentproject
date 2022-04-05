from flask import Flask, render_template,request

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
        return "success"
    return render_template("register.html")

@app.route('/search')
def Student_Search_page():
    return render_template("search.html")

@app.route('/delete')
def Student_Deletion_page():
    return render_template("delete.html")


if __name__== "__main__":
    app.run()
