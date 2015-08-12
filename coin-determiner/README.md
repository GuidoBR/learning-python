Coin-Determiner
================

It's a web application to determine the least number of coins, that when added, equal the input integer.

See it online at [Google App Engine](https://coin-determiner.appspot.com/)

## Instalation

1. Download source code
2. Activate the virtual env ``` source backend/venv/activate.sh ```
3. Run the server ``` dev_appserver.py backend/appengine ```

## CoinDeterminer

A function to determine the least number of coins that match the value of a given integer. See [coin docs](https://github.com/GuidoBR/coin-determiner/blob/master/backend/appengine/coin.py) for more.
Example:

### Input Test:
```
6
16
23
```

### Test Output:
```
2
2
3
```
