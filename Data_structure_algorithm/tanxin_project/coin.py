#!/usr/bin/env python3
import sys

def countcoins(money, coin: list, back_coins):
    coinsize = coin.pop()
    print(coinsize)
    cnt = money//coinsize
    print(cnt)
    back_coins[coinsize] = cnt
    print(back_coins)
    if money%coinsize == 0:
        print(back_coins)
        return back_coins
    else:
        r_money = money%coinsize
        countcoins(r_money, coin, back_coins)



# def getbackCoinCounts(money, coin: list):
#     cnt = 0
#     back_cons = {}
#     coin.sort(reverse=True)
#     if cons[-1] == 1:
#         print("error: the min cons is not eq 1")
#         sys.exit(1)
    
#     for i in money:
#         if money%i != 0 
    

if __name__ == "__main__":
   money = 69
   cons = [1,2,5,10]
 
   backcoin_cnt = countcoins(money,cons, backcoins)
   print(backcoins)

