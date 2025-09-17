from flask import Flask,render_template,request


app=Flask(__name__)



@app.route("/")
def home():
    return "<html><h1>Homepage</h1></html>"


@app.route("/index",methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello :{name}"
    
    return render_template('form.html')

@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
    
    
