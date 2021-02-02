def get_max_profit(prices):
max_so_far = 0 i = 2 for price in prices:
for next_price in prices[i::]: 
profit = next_price - price
if (profit > max_so_far):
max_so_far = profit 
i += 1 
return max_so_far; 
print(get_max_profit([1, 2, 5, 3]))

output: 4
