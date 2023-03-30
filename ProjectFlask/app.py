from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_proton():
    return "hello_proton, this is my first web"

if __name__=="__main__":
    app.run(host='0.0.0.0',degug=True)