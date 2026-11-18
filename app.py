from  flask import Flask,render_template,redirect,url_for,request,session
from database_services import create_note,remove_notes,update_notes,all_notes,note,user_data,create_user
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('secret_key')

@app.route("/")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    

    
    notes_data = all_notes(session["user_id"]) #pass session user_id here 
    result = [list(i) for i in notes_data]



    return render_template("dashboard.html",result = result)

@app.route("/add", methods = ["GET","POST"])            #add notes
def add():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        create_note(title,content,session["user_id"])

        return redirect(url_for("dashboard")) #redirect using function not html file address
    return render_template("add_notes.html")

@app.route("/remove/<int:id>",methods = ["POST"])
def remove(id):

    remove_notes(id)


    return redirect(url_for("dashboard"))


@app.route("/edit/<int:id>",methods = ["POST","GET"])
def edit(id):
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
    
        update_notes(id,title,content)


        return redirect(url_for("dashboard"))

    n = note(id)
    result = [list(i) for i in n] #preloaded data for form

    return render_template("edit.html",result = result,id = id)

@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/login",methods = ["POST","GET"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("pass")

        

        data = user_data(email)  

      
        if data and check_password_hash(data[2],password) :
            session["user_id"] = data[0]
            return redirect(url_for('dashboard'))
        else:
            return render_template("login.html",error = "invalid credentials ")
    
    return render_template("login.html")    


@app.route("/register", methods = ["POST","GET"])
def register():

    if request.method == "POST":
        gmail = request.form.get("gmail")
        password = request.form.get("pass")
        username = request.form.get("username")

        data = user_data(gmail)  


        if data is None:  #if email does'nt existed in database then register new user.
            hash_pass = generate_password_hash(password)
            create_user(gmail, hash_pass, username)
            return redirect(url_for('login'))
        else:
            return render_template(
            "register.html",
            error="Email already registered"
                                 )

    return render_template("register.html")

@app.route("/logout", methods = ["POST","GET"])
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
