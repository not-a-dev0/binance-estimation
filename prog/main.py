import datetime


def getSlResult(slLines,fPriceBuy,fPriceSell):
    # 1- Анализируемый список
    # 2- Цена покупки
    # 3- Цена продажи


    # флаг текущего состояния
    # готовность покупать - False
    # готовность продовать - True
    bFlOperation = False
    # количество первой валюты, просто для анализа прибыли при повторном использовании прибыли
    fCurrency = 100.00
    # прибыль
    fProfit = 0.00
    # количество сделок
    fDeal = 0.0
    # оборот
    fTurnover = 0.0

    for slLine in slLines:
        if not bFlOperation :
            if ( float(slLine[3]) < fPriceBuy ) and (float(slLine[2]) > fPriceBuy):
                # покупка
                bFlOperation = True
                fDeal += 0.5
                # print(datetime.datetime.fromtimestamp(int(slLine[0]) / 1e3),'BUY:',slLine[3],'sell',slLine[2],'volume',slLine[7],'Сделок',slLine[8])
        else:
            if ( float(slLine[3]) < fPriceSell ) and (float(slLine[2]) > fPriceSell) and (fPriceSell>fPriceBuy):
                # продажа
                bFlOperation = False
                fDeal += 0.5
                fProfit += (fPriceSell - fPriceBuy) * fCurrency
                # print(datetime.datetime.fromtimestamp(int(slLine[0]) / 1e3),'buy:',slLine[3],'SELL',slLine[2],'volume',slLine[7],'Сделок',slLine[8])
    return [fProfit,fPriceBuy,fPriceSell,fDeal]


from binance_api import Binance
bot = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

slKLines = bot.klines(
    symbol='ETHBTC',
    interval='12h',
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

# результирующий список
# 1 - покупка
# 2 - продажа
# 3 - прибыль
# 4 - количество сделок
# 5 - вариант
spResults = []
# номер варианта
iVersion = 0

j = i


while i>0:
    i-=1
    iTmp = j
    while j>0:
        j-=1
        spTmp = getSlResult(slKLines,float(spBuy[i]),float(spSell[j]))
        if spTmp[0]!=0.0:
            spResults.append(spTmp)
            iVersion += 1
    j = iTmp

spResults.sort(key=lambda ii: ii[0])
print(iVersion)
i=iVersion
while i>0:
    i-=1
    print(f"{iVersion-i} - P {(spResults[i][0]):4.8f} D {(spResults[i][3]):.1f} B {(spResults[i][1]):4.8f} S {(spResults[i][2]):4.8f}")