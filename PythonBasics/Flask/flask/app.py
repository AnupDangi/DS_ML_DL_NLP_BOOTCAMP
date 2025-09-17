from flask import Flask


app=Flask(__name__)


@app.route("/")
def home():
    return {"hello":"this is the  home page"}

@app.post("/form")
def get_form(user_id:str,email:str):
    return user_id,email


# print(f"This is {user_id}")

if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)
    
    
