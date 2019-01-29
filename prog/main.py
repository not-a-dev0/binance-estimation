import datetime


from binance_api import Binance
bot = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

slKLines = bot.klines(
    symbol='BNBBTC',
    interval='1d',
    limit=10)


# 
print('BNB/BTC 1d 10num')
i=0
# минимальная цена за весь период для покупки
fPriceMin = 99999999999999999.0
# максимальная цена за весь период для продажи
fPriceMax = 0.0
# уровни покупок
spBuy  = []
# уровни продаж
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

# флаг текущего состояния
# готовность покупать - False
# готовность продовать - True
bFlOperation = False
# количество первой валюты, просто для анализа прибыли
fCurrency = 100.00
# прибыль
fProfit = 0.00
# количество сделок
iDeal = 0



for slKLine in slKLines:
    if bFlOperation :
        pass
    else:
        pass
