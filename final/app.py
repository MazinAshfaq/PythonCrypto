from flask import Flask,render_template
import functions

app = Flask(__name__)

@app.route("/")
def home():
    data = functions.fetchData()
    return render_template("home.html", btc = data[0], eth=data[1])


if __name__ == "__main__":
    app.run()