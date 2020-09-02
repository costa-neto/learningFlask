from  flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<my_name>")
def greatings(my_name):
    return "Welcome "+my_name+"!"

@app.route("/square/<int:number>")
def show_square(number):
    return "Square of "+str(number)+" is: "+str(number*number)

@app.route("/educative")
def learn():
    return "Happy learning at educative!"

if __name__ == "__main__":
    app.run(debug = True, host="localhost", port=3000)