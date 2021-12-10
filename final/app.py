from flask import Flask
from pycoingecko import CoinGeckoAPI

# Create client 
cg = CoinGeckoAPI()

print(cg);
app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"


if __name__ == "__main__":
    app.run()