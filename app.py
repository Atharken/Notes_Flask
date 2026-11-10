from  flask import Flask,render_template,redirect,url_for,request
from database_services import create_note,remove_notes,update_notes,all_notes,note

app = Flask(__name__)

@app.route("/")
def dashboard():
    
    notes_data = all_notes()
    result = [list(i) for i in notes_data]



    return render_template("dashboard.html",result = result)

@app.route("/add", methods = ["GET","POST"])            #add notes
def add():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        create_note(title,content)

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
    result = [list(i) for i in n]

    return render_template("edit.html",result = result,id = id)

@app.route("/about")
def about():

    return render_template("about.html")




if __name__ == "__main__":
    app.run(debug=True)
