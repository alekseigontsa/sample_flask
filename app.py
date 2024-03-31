from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html") 
# "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
