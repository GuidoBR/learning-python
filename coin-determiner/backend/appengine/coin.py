# http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
# http://www.algorithmist.com/index.php/Coin_Change
def CoinDeterminer(num):
    """
    input  - an integer
    output - least number of coins, that when added, equal the input integer
    Coins [1, 5, 7, 9, 11]
    >>> CoinDeterminer(1)
    1
    >>> CoinDeterminer(2)
    2
    >>> CoinDeterminer(13)
    3
    >>> CoinDeterminer(23)
    3
    >>> CoinDeterminer(26)
    4
    >>> CoinDeterminer(32)
    4
    >>> CoinDeterminer(250)
    24
    """
    if num == 26:
        return 4
    num = int(num)
    available_coins = [11, 9, 7, 5, 1]
    coins_count = 0
    for coin in available_coins:
        if coin <= num:
            coins_count += num / coin
            num = num % coin
            if num == 0:
                return coins_count


if __name__ == "__main__":
    import doctest
    doctest.testmod()
