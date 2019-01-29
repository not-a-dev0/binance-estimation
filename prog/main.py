import datetime


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
fPriceMin = 99999999999999999.0
fPriceMax = 0.0
spBuy  = []
spSell = []

for slKLine in slKLines:
    i+=1
    print(i,datetime.datetime.fromtimestamp(int(slKLine[0]) / 1e3),'buy:',slKLine[3],'sell',slKLine[2],'volume',slKLine[7],'Сделок',slKLine[8])
    spBuy.append(float(slKLine[3]))
    spSell.append(float(slKLine[2]))
    
    
    if float(slKLine[3]) < fPriceMin:
        fPriceMin = float(slKLine[3])
    if float(slKLine[2]) > fPriceMax:
        fPriceMax = float(slKLine[2])


print ('min=', fPriceMin, 'max=', fPriceMax)

print(spBuy)
print(spSell)

