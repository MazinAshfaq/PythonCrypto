from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

cg.get_price(ids='bitcoin', vs_currencies='usd')
