from flask import Flask,render_template
import functions

app = Flask(__name__)

@app.route("/")
def home():
    coinTable = functions.fetchCoins()
    return render_template("home.html", coinTable = coinTable)

@app.route("/Charts")
def chart():
    data = functions.fetchChartData()
    return render_template("chart.html", btc = data[0], eth=data[1])


if __name__ == "__main__":
    app.run()