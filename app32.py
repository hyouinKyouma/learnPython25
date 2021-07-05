from flask import Flask
print(__name__)
app = Flask(__name__)
# app.debug = False 
# print(__name__)

@app.route("/")
def hello_world():
   
    return "<p>Hello, app 32!</p>"
