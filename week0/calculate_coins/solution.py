def calculate_coins(n):
    coins = {1:0, 2:0, 100:0, 5:0, 10:0, 50:0, 20:0}
    n = int(n * 100)
    keys = sorted(coins, key = coins.get)
    for i in list(reversed(sorted(keys))):
        if n // i >= 1:
            coins[i] = n // i
            n = n % i
        else:
            coins[i]=0 
    return coins
