from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Student_Login_page():
    return render_template("login.html")

@app.route('/register')
def Student_Registration_page():
    return render_template("register.html")

@app.route('/search')
def Student_Search_page():
    return render_template("search.html")

@app.route('/delete')
def Student_Deletion_page():
    return render_template("delete.html")


if __name__== "__main__":
    app.run()
