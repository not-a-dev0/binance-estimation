from binance_api import Binance
bot = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

print('klines', bot.klines(
    symbol='BNBBTC',
    interval='1d',
    limit=4
))
