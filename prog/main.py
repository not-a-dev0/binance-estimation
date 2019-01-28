from datetime import datetime


from binance_api import Binance
bot = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

slKLines = bot.klines(
    symbol='BNBBTC',
    interval='1d',
    limit=20)


# 
print('BNB/BTC 1d 4num')
i=0
for slKLine in slKLines:
    i+=1
    print(i,'Дата:',str(datetime.fromtimestamp(int(slKLine[0]))),'Покупка:',slKLine[3],'Продажа',slKLine[2],'Обьем',slKLine[7],'Сделок',slKLine[8])