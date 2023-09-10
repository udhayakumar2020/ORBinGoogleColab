
# WHOLE WROMG ITS JUST BACKTESTING WE NEED TO CHANGE AS A LIVE PRICE TO TRADE IN LICE AND CURRENT PRICe

# =>Issue =>in cipla sorting sorting all issue i think dude
# =>Need a buffers.01 and stopentry at after 10:20 


# Need a single symbol to take a month or year data to test which scripts are suitable with which R:R and SL:TR:


print("you can!!")
print(
    'Loot of scripts are found there but all are not good for a intraday ORB strategy right res lets choose a best ones '
)
import login as login
from datetime import datetime
import time
import os
import time
import json
from niftystocks import ns
import math

true = True
loss = 0
profit = 0
symbolsinlongprofit = []
symbolsinlongloss = []
symbolsinshortloss = []
symbolsinshortprofit = []
symbolsindraw=[]
high = []
wholeEntries=0
lbuffer = 0
No_entry =0
wins=0
losses=0
draw=0
longLPts=0
longPPts=0
shortLPts=0
shortPPts=0
higherHigh=0
print("LOGGED-IN")
# symbols = [
#     'NSE:SBIN-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:AXISBANK-EQ', 'NSE:HDFCBANK-EQ',
#     'NSE:ICICIBANK-EQ', 'NSE:LT-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:INDUSINDBK-EQ',
#     'NSE:HDFC-EQ', 'NSE:HINDALCO-EQ', 'NSE:TITAN-EQ', 'NSE:TCS-EQ',
#     'NSE:POWERGRID-EQ', 'NSE:WIPRO-EQ', 'NSE:INFY-EQ', 'NSE:TECHM-EQ'
# ]
symbols = ['NSE:AXISBANK-EQ', 'NSE:BAJAJ-AUTO-EQ', 'NSE:BHARTIARTL-EQ', 'NSE:BPCL-EQ', 'NSE:CIPLA-EQ', 'NSE:COALINDIA-EQ', 'NSE:EICHERMOT-EQ', 'NSE:GRASIM-EQ', 'NSE:HCLTECH-EQ', 'NSE:HDFCLIFE-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:HINDUNILVR-EQ', 'NSE:ICICIBANK-EQ', 'NSE:INDUSINDBK-EQ', 'NSE:INFY-EQ', 'NSE:IOC-EQ', 'NSE:ITC-EQ', 'NSE:JSWSTEEL-EQ', 'NSE:KOTAKBANK-EQ', 'NSE:LT-EQ', 'NSE:M&M-EQ', 'NSE:NTPC-EQ', 'NSE:RELIANCE-EQ', 'NSE:SBILIFE-EQ', 'NSE:SBIN-EQ', 'NSE:SUNPHARMA-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATAMOTORS-EQ', 'NSE:TATASTEEL-EQ', 'NSE:TCS-EQ', 'NSE:TECHM-EQ', 'NSE:TITAN-EQ', 'NSE:UPL-EQ']
# janhighproba=['NSE:ASIANPAINT-EQ','NSE:HDFC-EQ','NSE:HDFCBANK-EQ','NSE:EICHERMOT-EQ','NSE:COALINDIA-EQ','NSE:INDUSINDBK-EQ','NSE:SBIN-EQ','NSE:ICICIBANK-EQ','NSE:MARUTI-EQ','NSE:BAJAJFINSV-EQ','NSE:HINDUNILVR-EQ','NSE:JSWSTEEL-EQ','NSE:HDFCLIFE-EQ','NSE:M&M-EQ','NSE:INFY-EQ','NSE:BAJAJ-AUTO-EQ','NSE:BHARTIARTL-EQ','NSE:KOTAKBANK-EQ','NSE:POWERGRID-EQ','NSE:RELIANCE-EQ']
# symbols=janhighproba
# symbols=['NSE:HDFC-EQ', 'NSE:HDFCBANK-EQ','NSE:AXISBANK-EQ', 'NSE:GRASIM-EQ', 'NSE:HEROMOTOCO-EQ', 'NSE:HINDALCO-EQ', 'NSE:ICICIBANK-EQ', 'NSE:ITC-EQ', 'NSE:SBIN-EQ', 'NSE:TATACONSUM-EQ', 'NSE:TATASTEEL-EQ']  
# symbols= ['NSE:NIFTY50-INDEX']
# symbols= ['NSE:ADANIPORTS-EQ']
symbols= ['NSE:BPCL-EQ']
# OHLC


def data_handling(symbol):
    # date = '2023-01-20'
    date = datetime.today().strftime('%Y-%m-%d')
    date = '2023-09-08'

    hist_data = {
        "symbol": symbol,
        "resolution": "1",
        "date_format": 1,
        "range_from": date,
        "range_to": date,
        "cont_flag": "1"
    }
    srp = login.fyers.history(hist_data)
    # print(srp)
    hl_data = srp["candles"][0]
    high = hl_data[2]
    low = hl_data[3]
    # print("High:", high, "  ", "Low:", low)
    return high, low, srp


# data_handling("NSE:SBIN-EQ")


def place_orders(symbol, h, l, day30M):
    with open('BPCL1m.txt','r') as f:
    
        var = f.read() 
        # print(var[0])  
        YDC = 0


    # df = {"symbols":symbol}
    # print(df)
    # SYdata = login.fyers.quotes(df)["d"]
    # YDC = SYdata[0]["v"]['prev_close_price']
    # print(ltp)
    # print(SYdata)
    
    
    lSL =  h- (h * .003)    
    print("slll",lSL)
    sSL = round(l * .003)
    lTR = round(h * .050)
    sTR = round(l * .050)
    
    global lbuffer
    
    lbuffer = math.floor( l * .001)
    lbuffer = 0

    # print(lbuffer)
    hbuffer = round( 0)
    lbuffer = 0
    hbuffer = 0

    global longLPts
    global longPPts
    global shortLPts
    global shortPPts
    profitAmount=200
    lossAmount=100
    long = False
    short = False
    global loss
    global profit
    global wholeEntries 
    traded = False
    candle = 0
    IS_TLSL=False
    
    
    global wins
    global losses
    global draw
    global No_entry
    global higherHigh

    var = day30M['candles'] 
    # with open('BPCL1m.txt','w') as f:
    #     f.write(str(var)) 
        # here we need to loop all the candle to find the entry and exit to calculate profit and loss
    totalCandle = len(var)
    for i in var:

        candle += 1  #with variable candle u can diable the afternoon trades or change range
        # print('Current candle:',candle)
        opening = i[1]
        high = i[2]
        low = i[3]
        lbuff = l * .001
        hbuff = h * .001
        close = i[4]
        volume = i[5]
        number = int(close)


        # long=False
        # short=False
        # traded=False
        # print(i ,'high=',high , 'low',low)
        # print()
        def trade():
            pass

        if traded != True:
            # + hbuff and candle < 4and high > YDC and low < YDC
            if high > h and candle <= 6 and h > YDC:
                # p
                # symbols.remove(symbol)
                print(f'Long in {symbol}')
                # with open('trades.txt','a') as Entrysctipt:
                #     Entrysctipt.write("'"+symbol+"'"+',')
                    
                traded = True
                long = True
                wholeEntries +=1
                continue
            elif low < (l ) and candle <= 6 and l < YDC:
                # symbols.remove(symbol)
                # - lbuff and candle< 4
                print(f"Sort in {symbol} at:{l-lbuffer}")
                # print(f'{symbol}Selling at{low} with SL__ TRG__ ')
                wholeEntries +=1
                traded = True
                short = True
                continue
            # elif candle > 6:
            # #which helps in avoiding late entries
            #     break
            elif candle == totalCandle:
                draw +=1
                No_entry +=1 
                pass
                # print(f'range Bound in candle {candle}')
                
                
        elif short == True:

            if high > l + sSL:
                shortLPts+=sSL

                losses +=1
                loss += lossAmount
                symbolsinshortloss.append(symbol)
                print(
                    f'{symbol}Loss in candle:{candle} SORTING at{l}  Sl{l+sSL} TRG{l-sTR} ShortLosspts:{shortLPts}'
                )

                break
            elif low < l - sTR:
                # print(sTR)
                shortPPts+=sTR

                wins +=1
                profit += profitAmount
                symbolsinshortprofit.append(symbol)

                print(
                    f'{symbol}Profit in candle:{candle} SORTING at{l} Sl{l+sSL} TRG{l-sTR} Shortprofit{sTR}'
                )
                break
            elif candle == totalCandle:
                draw +=1
                symbolsindraw.append(symbol)
                shortPPts +=int(low - l)
                wins +=1
                # drawpoint = float(l[0]) - float(close[0])
                # drawpoint = float(l) - float(close)

                # print(f'drawPoints:{drawpoint}')
            
                # wins +=1
                print("CLOSED AT EOD Short")
                break
            
            elif low < l  :
                # wins +=1
                # wholeEntries +=-1

                print( l +(sTR / 2 ))
                print(f'in profit  candle{candle} & SL been updated')
                sSL = round(l * .001) 

            # elif 
        elif long == True:
            print('current SL & candle',lSL ,candle , )
            # print('num',number)
            # print(higherHigh)
            # print(number >= higherHigh)
            if (number > higherHigh):
                IS_TLSL=True
                higherHigh = number
                print('HH',higherHigh)
                lSL = higherHigh-(higherHigh * .006) 
                print('TSL',lSL)
                
            if high > h + lTR:
               
                wins +=1
                profit += profitAmount
                symbolsinlongprofit.append(symbol)
                # print(symbolsinlongprofit)
                longPPts+=lTR
                
                # print(
                #     f'Targeeet {symbol}Profit in candle{candle},LONG signal @ {h}  Sl{h-lSL} TRG{h+lTR}  PTSstatic:{longPPts}'
                # )
                break
            
            
            # elif candle == totalCandle or  high == h:
            #     # this works onlt EOD
            #     longPPts += int(high -h)
            #     symbolsindraw.append(symbol)
            #     # drawpoint = h - close   
            #     # print(f'drawPoints:{drawpoint}')
                
            #     draw +=1
            #     wins +=1
            #     print("EXITED WITH SQUARE OFF Long EOD")
            #     break
            
            
            elif low < lSL:
                if IS_TLSL:
                    
                    wins +=1
                    profit += profitAmount
                    symbolsinlongprofit.append(symbol)
                    # print(symbolsinlongprofit)
                    longPPts+=lTR
                    
                    print(
                        f'Target/IS_TLSL {symbol}Profit in candle{candle},LONG signal @ {h}  Sl{h-lSL} TRG{h+lTR}  PTSstatic:{longPPts}'
                    )
                    break
                else:
                    losses +=1
                    loss += lossAmount
                    symbolsinlongloss.append(symbol)
                    longLPts+=lSL
                    print('profit',lSL - h)
                    print(
                        f'TSL {symbol}Loss in candle{candle} LONG signal at{h + hbuffer} entry{h} Sl{lSL} TRG{h+lTR} lossptsStatic:{h-lSL} '
                    )

                    break
           
            elif high > higherHigh:
                # wins +=1
                # wholeEntries +=-1

                # print( h +(lTR / 2 )) #above half traget sl changes
                
                # lSL += (higherHigh * 0.001)
                
                # lSL = (high * 0.002) + h
                

                
                # print((high * 0.01))
                # print(dummy ,high,lSL)

                print(f'{symbol} in profit  candle {candle} & SL been updated as: {lSL} high: {high}')
                
            
    # 13 30mins candle in a day
    # print("VAR:",var)
    ltp = var[0]

    # print("LTP:", ltp)
    # if ltp>h:
    #     print("Placing buy market cover order!")
    # elif ltp<l:
    #     print("Placing sell market cover order!")
    # else:
    #     print("Price between Opening Range High and Low!")


start = "09:45:00"
end = "15:00:00"
now = datetime.strftime(datetime.now(), "%H:%M:%S")

# Check is it need to run a code in range of 9:40 - 3:30
run = True if ((now > start) & (now < end)) else False

# next line i aded back test
run = True

if run == False and now < start:
    x = True
    while x:
        print("Waiting for market to open")
        time.sleep(60)
        now = datetime.strftime(datetime.now(), "%H:%M:%S")
        x = True if now < start else False
    run = True

while run:
    print("\nCurrent time", "   ", now)
    for i in symbols:
        print("\n" + i)
        h,l,day30M = data_handling(i)
        place_orders(i, h, l, day30M)
    print("profit total   :", profit)
    print('loss total     :', loss)
    print('DRAW total     :', draw)
    print('Total entries  :',wholeEntries)
    print('Brokerages     :',wholeEntries * 20)
    print('AfterBrokerages:',profit - loss -(wholeEntries * 5))
    # print("Total$:",profit - loss)
    # print(symbols)
    # time.sleep(30)

    now = datetime.strftime(datetime.now(), "%H:%M:%S")
    # run = True if ((now > start) & (now < end)) else False
    run = False 

print("symbolsinshortprofit :", symbolsinshortprofit)
print("symbolsinshortloss   :", symbolsinshortloss)
print("symbolsinlongprofit  :", symbolsinlongprofit)
print('symbolsinlongloss    :', symbolsinlongloss)
print('no entries           :', No_entry)
print("symbolsinshortprofit :", shortPPts)
print("symbolsinshortloss   :", shortLPts)
print("symbolsinlongprofit  :", longPPts)
print('symbolsinlongloss    :', longLPts)
print('Probabilityof win    :' ,wins / (wins+losses) *100)

if now > end:
    print("\nMarket Closed!")




# with open('ExcelUi.csv', 'a') as csvfile:
#                     FieldName = [
#                         'Name', 'Entryprice', 'Exitprice', 'side', 'status'
#                     ]
#                     theWritter = csv.DictWriter(csvfile, fieldnames=FieldName)
#                     theWritter.writeheader()
#                     theWritter.writerow({
#                         'Name': symbol,
#                         'Entryprice': h,
#                         'Exitprice': low,
#                         'side': 'long',
#                         'status': 'loss'
#                     })

#  with open('ExcelUi.csv', 'a') as csvfile:
#                     FieldName = [
#                         'Name', 'Entryprice', 'Exitprice', 'side', 'status'
#                     ]
#                     theWritter = csv.DictWriter(csvfile, fieldnames=FieldName)
#                     theWritter.writeheader()
#                     theWritter.writerow({
#                         'Name': symbol,
#                         'Entryprice': h,
#                         'Exitprice': high,
#                         'side': 'long',
#                         'status': 'Profit'
#                     })







def place_ordersss(symbol, h, l, day30M):
    df = {"symbols": symbol}
    SYdata = login.fyers.quotes(df)["d"]
    YDC = SYdata[0]["v"]['prev_close_price']

    lSL = h * 0.002 + h
    sSL = round(l * 0.002)
    lTR = round(h * 0.050)
    sTR = round(l * 0.010)

    global lbuffer
    lbuffer = 0

    global longLPts, longPPts, shortLPts, shortPPts,loss, profit, wholeEntries, traded, candle,wins, losses, draw, No_entry, higherHigh
    profitAmount = 200
    lossAmount = 100
    long = False
    short = False
    traded = False
    candle = 0

    var = day30M['candles']
    totalCandle = len(var)

    for i in var:
        candle += 1

        opening = i[1]
        high = i[2]
        low = i[3]
        close = i[4]
        volume = i[5]

        if traded is not True:
            if high > h and candle <= 6 and h > YDC:
                print(f'Long in {symbol}')
                traded = True
                long = True
                wholeEntries += 1
                continue
            elif low < (l) and candle <= 6 and l < YDC:
                print(f"Short in {symbol} at:{l-lbuffer}")
                wholeEntries += 1
                traded = True
                short = True
                continue
            elif candle == totalCandle:
                draw += 1
                No_entry += 1
                pass
       
       
        elif short == True:
            if high > l + sSL:
                shortLPts += sSL
                losses += 1
                loss += lossAmount
                symbolsinshortloss.append(symbol)
                break
            elif low < l - sTR:
                shortPPts += sTR
                wins += 1
                profit += profitAmount
                symbolsinshortprofit.append(symbol)
                break
            elif candle == totalCandle:
                draw += 1
                symbolsindraw.append(symbol)
                shortPPts += int(low - l)
                wins += 1
                break
            elif low < l:
                print(l + (sTR / 2))
                print(f'in profit  candle{candle} & SL been updated')
                sSL = round(l * 0.001)
        elif long == True:
            number = int(high)
            if number > higherHigh:
                higherHigh = number
                print('HH', higherHigh)
                lSL = higherHigh - (higherHigh * 0.003)
                print('TSL', lSL)
            if high > h + lTR: 
                wins += 1
                profit += profitAmount
                symbolsinlongprofit.append(symbol)
                longPPts += lTR
                break
            elif low < lSL:
                losses += 1
                loss += lossAmount
                symbolsinlongloss.append(symbol)
                longLPts += lSL
                print(f'TSL {symbol}Loss in candle{candle} LONG signal at{h + hbuffer} entry{h} Sl{lSL} TRG{h+lTR} lossptsStatic:{h-lSL}')
                break
            elif high > higherHigh:
                print(f'{symbol} in profit  candle {candle} & SL been updated as: {lSL} high: {high}')
