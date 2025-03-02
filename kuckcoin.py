#!/bin/env python3

import json
import argparse
import requests
from os import system
from time import sleep

space=' '

def kucoin_logo():
    with open('kucoin.uni') as logoFile:
        logo = logoFile.readlines()
    for line in logo:
        print(10*space,line, end='')
        
def get_kucoin_order_books(coin1, coin2, args):
    KuOrderBk='https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=%s-%s'
    
    ku_response = requests.get(KuOrderBk % (coin1, coin2)) 
    
    
    if ku_response.status_code == 200:
        try:
            KuJSON = json.loads(str(ku_response.content.decode('utf-8')))
            KuBids = KuJSON['data']['bids']
            KuAsks = KuJSON['data']['asks']
            kucoin_logo()
            print("                          %4s - %4s                             " % (coin1, coin2))
            print("_____________BIDS_____________ | _____________ASKS_____________")
            k=0
            for bid in KuBids:
                print("{0:<18.6f}{1:>12.4f}{2:>13.6f}{3:>20.4f}".format(float(bid[0]),
                                                                       float(bid[1]),
                                                                       float(KuAsks[k][0]),
                                                                       float(KuAsks[k][1])),
                                                                       flush=True)
                k += 1
                
                
        except:
            print("error reading JSON")
            

def main():
    parser = argparse.ArgumentParser(description="KuCoin - Order Books for Trading Pair")

    parser.add_argument('coins', metavar='coin', nargs='+')
    parser.add_argument('-t', '--time', help="Time in seconds to refresh orderbook, default 300", metavar='target')
    args = parser.parse_args()
    
    coin1 = args.coins[0]
    coin2 = args.coins[1]
    
    if args.time:
        refresh = int(args.time)
    else:
        refresh = 300
        
    while True:
        system('cls||clear')
        get_kucoin_order_books(coin1, coin2, args)
        sleep(refresh)


if __name__ == "__main__":
    main()

