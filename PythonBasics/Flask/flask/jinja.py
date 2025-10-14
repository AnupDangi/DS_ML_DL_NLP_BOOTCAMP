## Building Ulr Dynamically
## Vairable Rule
### Jinja 2 Template Engine

'''
{{ }} expresions to print output in html 
{%...%} conditions, for loops 
{#...#} this is for comments
'''

from flask import Flask,render_template,request


app=Flask(__name__)


@app.route("/")
def home():
    return "<html><h1>Homepage</h1></html>"


@app.route('/success/<int:score>')
def success(score):
    res=""
    if(score>=50):
        res="Pass"
    else:
        res="FAIL"
    
    exp={'score':score,'res':res}
    return render_template('result1.html',results=exp)

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8001,debug=True)
    

@app.route("/fail/<int:score>")
def fail(score):
    return render_template("result.html",results=score)

