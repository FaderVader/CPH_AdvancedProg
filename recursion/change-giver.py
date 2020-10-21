def give_change(amount):
    if amount < 0: raise ValueError
    if amount == 0: return 0
    if amount > 98000: raise ValueError

    denomonations = [100, 50, 25, 10, 5, 1]

    def getListOfCoins(amount, return_coins = []):
        if amount == 0: return 0
        for coin in denomonations:
            if amount // coin > 0:
                return_coins.append(coin)
                getListOfCoins(amount - coin, return_coins)
                break
        return return_coins

    def getDictOfCoins(lst_coins, dict_coins): # recurse over list-content, inc value in dict-match
        if lst_coins == []: return []
        dict_coins[lst_coins.pop()] += 1
        getDictOfCoins(lst_coins, dict_coins)

    return_coins = getListOfCoins(amount)
    dict_coins = dict.fromkeys(return_coins, 0) # build dict of coins in list
    getDictOfCoins(return_coins, dict_coins)
    return dict_coins

for k,v in give_change(393).items():
    print(f'Give {v} of {k}')