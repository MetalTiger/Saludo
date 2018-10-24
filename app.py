from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "K T pasa klabaza"
 
if __name__ == "__main__":
    app.run()
