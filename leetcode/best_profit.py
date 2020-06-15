prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
# curr_profit = prices[0]
# max_profit = prices[0]
# for i in range(1, len(prices)):
#     if prices[i] < curr_profit:
#         curr_profit += 
# print(max_profit)
i = 0
profit = 0
n = len(prices)
while i < n - 1:
    if prices[i + 1] > prices[i]:
        j = i + 1
        while j < n and prices[j] > prices[j - 1]:
            j += 1
        print(i, j, prices[i], prices[j - 1], profit)
        profit += prices[j - 1] - prices[i]
        i = j - 1
    i += 1
print(profit)