# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# method 1
def maxProfit(prices):
    profit =  0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] > prices[i]:
                profit = max(profit,prices[j] - prices[i]) 
    if profit > 0:                   
        return profit  
    return 0     

# method 2
def max_profit(arr):
    maxPro = 0
    # Since infinity cannot be represented by a number in programming languages, the float() function is used to represent an infinite integer in the form of float(inf). It converts the string infinity value to a floating infinity value
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
print(max_profit(prices))
