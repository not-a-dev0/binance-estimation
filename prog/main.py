import datetime


from binance_api import Binance
bot = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

slKLines = bot.klines(
    symbol='BNBBTC',
    interval='1d',
    limit=100)


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
    # print(i,datetime.datetime.fromtimestamp(int(slKLine[0]) / 1e3),'buy:',slKLine[3],'sell',slKLine[2],'volume',slKLine[7],'Сделок',slKLine[8])
    spBuy.append(float(slKLine[3]))
    spSell.append(float(slKLine[2]))
    
    
    if float(slKLine[3]) < fPriceMin:
        fPriceMin = float(slKLine[3])
    if float(slKLine[2]) > fPriceMax:
        fPriceMax = float(slKLine[2])


# print ('min=', fPriceMin, 'max=', fPriceMax)

# print(spBuy)
# print(spSell)

# флаг текущего состояния
# готовность покупать - False
# готовность продовать - True
bFlOperation = False
# количество первой валюты, просто для анализа прибыли
fCurrency = 100.00
# прибыль
fProfit = 0.00
# количество сделок
fDeal = 0.0
# цена покупки
fPriceBuy = 0.00155
# цена продажи
fPriceSell = 0.00161
# оборот
fTurnover = 0.0

for slKLine in slKLines:
    if not bFlOperation :
        if ( float(slKLine[3]) < fPriceBuy ) and (float(slKLine[2]) > fPriceBuy):
            # покупка
            bFlOperation = True
            fDeal += 0.5
            print(i,datetime.datetime.fromtimestamp(int(slKLine[0]) / 1e3),'BUY:',slKLine[3],'sell',slKLine[2],'volume',slKLine[7],'Сделок',slKLine[8])
    else:
        if ( float(slKLine[3]) < fPriceSell ) and (float(slKLine[2]) > fPriceSell):
            # продажа
            bFlOperation = False
            fDeal += 0.5
            fProfit += (fPriceSell - fPriceBuy) * fCurrency
            print(i,datetime.datetime.fromtimestamp(int(slKLine[0]) / 1e3),'buy:',slKLine[3],'SELL',slKLine[2],'volume',slKLine[7],'Сделок',slKLine[8])


print ('Profit',fProfit,'Deal',fDeal)
        

