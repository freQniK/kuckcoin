# kuckcoin

Display Kucoin Orderbooks for a Coin Pair in  Terminal



# Run

```shell
usage: kuckcoin.py [-h] [-t target] coin [coin ...]

KuCoin - Order Books for Trading Pair

positional arguments:
  coin

optional arguments:
  -h, --help            show this help message and exit
  -t target, --time target
                        Time in seconds to refresh orderbook, default 300
```

Example:

```shell
python3 kuckcoin.py -t 600 DVPN USDT
```

Result:



```shell
       ⣴⡄⠀⣴⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
       ⣿⣧⣾⡿⠋⠻⣿⡆⠀⠀⣿⢠⣾⠋⢸⣿⠀⣿⡇⢰⣿⠿⣷⢀⣾⠿⣷⡄⢸⣿⠀⣿⣦⢸⣿
       ⣿⣿⣿⠀⣿⡇⢈⠀⠀⠀⣿⣿⣧⠀⢸⣿⠀⣿⡇⢸⡇⠀⠀⢸⣿⠀⣿⡇⢸⣿⠀⣿⣻⣿⣿
       ⣿⡟⢿⣷⣄⣴⣿⠇⠀⠀⣿⠀⢻⣇⠘⢿⣶⡿⠃⠸⣷⣶⡿⠈⢿⣶⡿⠃⢸⣿⠀⣿⠇⢻⣿
       ⠻⠃⠀⠻⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
                      DVPN - USDT                             
_____________BIDS_____________ | _____________ASKS_____________
0.000376           339245.0079     0.000377         123075.2917
0.000376           330128.1961     0.000377         131368.3278
0.000375           659836.5620     0.000377         799572.7732
0.000372           265463.2333     0.000377        3575069.0539
0.000372           285759.1523     0.000379          12014.1823
0.000370            30000.0000     0.000384          11879.2069
0.000370           441730.4869     0.000386          43091.8394
0.000369            30000.0000     0.000386          53601.2923
0.000369           533543.2724     0.000389           1062.0676
0.000368            42145.4125     0.000390          40740.9070
0.000367            78000.0000     0.000392         110000.0000
0.000367           284337.1088     0.000392          29000.0000
0.000367            30000.0000     0.000392         357142.8571
0.000367            78000.0000     0.000392          29000.0000
0.000367           457072.7463     0.000395         612956.0542
0.000366            48000.0000     0.000396          11599.6823
0.000365            79000.0000     0.000396          52247.6538
0.000365            31000.0000     0.000402          11455.9114
0.000365            54981.7091     0.000404         100000.0000
0.000364              803.0000     0.000407          50934.8321
```
```

This will fetch the orderbook every 600 seconds and redraw the screen.
