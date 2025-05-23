#Brute forece
'''
prices=[7,2,1,11]
n=len(prices)
maxi=0
for i in range(0,n-1):
    total=0
    for j in range(i+1,n):            #time --> n*n
        total=prices[j]-prices[i]
        maxi=max(total,maxi)
print(maxi)    
'''

prices = [7, 2, 1, 5, 6, 4, 12]
n = len(prices)
maxi_profit = 0
min_price = float("inf")

for i in range(n):
    min_price = min(min_price, prices[i])
    profit = prices[i] - min_price
    maxi_profit = max(maxi_profit, profit)

print(maxi_profit)
