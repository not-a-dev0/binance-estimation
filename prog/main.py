import datetime


def getSlResult(slLines,fPriceBuyF,fPriceSellF):
    # 1- Анализируемый список
    # 2- Цена покупки
    # 3- Цена продажи


    # флаг текущего состояния
    # готовность покупать - False
    # готовность продавать - True
    bFlOperation = False
    # количество первой валюты, просто для анализа прибыли при повторном использовании прибыли
    fCurrency = 1.00
    # прибыль
    fProfit = 0.00
    # количество сделок
    fDeal = 0.0
    # оборот
    fTurnover = 0.0

    fMoneyF = 1000

    for slLine in slLines:
        if not bFlOperation :
            if ( float(slLine[3]) < fPriceBuyF ) and (float(slLine[2]) > fPriceBuyF):
                # покупка
                bFlOperation = True
                fDeal += 0.5
        else:
            if ( float(slLine[3]) < fPriceSellF ) and (float(slLine[2]) > fPriceSellF) and (fPriceSellF>fPriceBuyF):
                # продажа
                bFlOperation = False
                fDeal += 0.5
                fProfit +=  fMoneyF / fPriceBuyF * fPriceSellF  - fMoneyF
    
    fProfit = fProfit/fMoneyF * 100
    
    return [fProfit,fPriceBuyF,fPriceSellF,fDeal]


# исходные данные ----------------
# валютная пара 
sPair = 'EOSUSDC'
# количество интервалов для анализа
iLimit = 180
# интервал 
sInterval = '2h'
# количество результатов для выдачи
iCountPrint = 5



from binance_api import Binance
bot = Binance(
    API_KEY='D7...Ejj',
    API_SECRET='gwQ...u3A'
)

slKLines = bot.klines(
    symbol=sPair,
    interval=sInterval,
    limit=iLimit)



print(f'Анализируем пару {sPair} на интервале {sInterval} лимитом {iLimit}')

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

# Сортируем по максиму прибыли
spResults.sort(key=lambda ii: ii[0])


# Выводим результирующие данные
print(f'Расчитано {iVersion} позитивных вариантов. Колебание цены от {fPriceMin:.8f} до {fPriceMax:.8f}')

print (f'\nАбсолютный рейтинг из {iCountPrint} позиций по прибыли:')
i=iVersion
iTmpCountPrint = iCountPrint


while (i>0) and (iTmpCountPrint>0):
    i-=1
    iTmpCountPrint-=1
    print(f"{iVersion-i} - {(spResults[i][0]):.2f}% {(spResults[i][3]):.1f} сделок покупка:{(spResults[i][1]):4.8f}  продажа:{(spResults[i][2]):4.8f}")

print (f'\nРейтинг из {iCountPrint} позиций среди закрытых сделок по прибыли:')
i=iVersion
iTmpCountPrint = iCountPrint

while (i>0) and (iTmpCountPrint>0):
    i-=1
    if int(spResults[i][3]) == (spResults[i][3]) :
        iTmpCountPrint-=1
        print(f"{iVersion-i} - {(spResults[i][0]):.2f}% {(spResults[i][3]):.1f} сделок покупка:{(spResults[i][1]):4.8f}  продажа:{(spResults[i][2]):4.8f}")

# сортируем по максимальному количеству сделок
spResults.sort(key=lambda ii: ii[3])


print (f'\nАбсолютный рейтинг из {iCountPrint} позиций по кол-ву сделок:')
i=iVersion
iTmpCountPrint = iCountPrint


while (i>0) and (iTmpCountPrint>0):
    i-=1
    iTmpCountPrint-=1
    print(f"{iVersion-i} - {(spResults[i][0]):.2f}% {(spResults[i][3]):.1f} сделок покупка:{(spResults[i][1]):4.8f}  продажа:{(spResults[i][2]):4.8f}")

print (f'\nРейтинг из {iCountPrint} позиций среди закрытых сделок по кол-ву сделок:')
i=iVersion
iTmpCountPrint = iCountPrint

while (i>0) and (iTmpCountPrint>0):
    i-=1
    if int(spResults[i][3]) == (spResults[i][3]) :
        iTmpCountPrint-=1
        print(f"{iVersion-i} - {(spResults[i][0]):.2f}% {(spResults[i][3]):.1f} сделок покупка:{(spResults[i][1]):4.8f}  продажа:{(spResults[i][2]):4.8f}")

print ('\n')