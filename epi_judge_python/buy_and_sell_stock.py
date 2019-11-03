from test_framework import generic_test

# 5.6
def buy_and_sell_stock_once(prices):
    max_profit = 0.0
    low = prices[0]
    
    for price in prices:
        profit = price - low
        if max_profit < profit:
            max_profit = profit
        low = min(low, price)
        
    
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
