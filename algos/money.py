def get_min_change(denominations, total):
    denominations.sort(reverse=True)
    coins_needed = 0
    for dem in denominations:
        if dem <= total:
            fit = total / dem
            coins_needed += fit
            total -= fit * dem
    return coins_needed

def dyn_min_change(money, coins):
    minCoins = {0: 0}
    for i in range(1, money + 1):
        minCoins[i] = Ellipsis
        for coin in filter(lambda x: x <= i, coins):
            # the subproblem here becomes
            # to find the min change needed for money
            # gotta find the min among the change needed
            # for money - each denomination
            change = minCoins[i - coin] + 1
            if change < minCoins[i]:
                minCoins[i] = change
    return minCoins[money]
