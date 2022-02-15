"""
    A Burglar breaks into a house with a bag that can carry a 
    maximum of 20 kg. He found a safe with 8 gold pellets with the following 
    weights and their corresponding values in US$:

5kg - $2500
3kg -$1700
1kg-$1200
6kg-$3000
8kg-$4100
4kg-$2000
11kg-$7000
12kg-$7500
 

Using the 0-1 Knapsack Algorithm , 
which combination of pellets would bring about the highest profit, provided 
the weight does not exceed 20kgs. 
Print the combination of the pellets and the total value accrued by that combination. [5]
"""


# Solving problem using Greedy method

weight = 20 # weight check to ensure our constraint doesn't exceed 
max_profit = 0
# a list of items weights
weights = [5, 3, 1, 6, 8, 4, 11, 12]


# create list of prices corresponding prices to corresponding index of weight
profit = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]

# list of price per kg
profit_per_kg = []
for i in range(len(weights)):
    profit_per_kg.append(round(profit[i]/weights[i], 2))


# choosing items to insert into knapsack
robbery_loot = []

while weight != 0:
    num = profit_per_kg.index(max(profit_per_kg))
    item = profit_per_kg.pop(num)
    if weights[num] < weight:

        robbery_loot.append(weights[num])
     
        weight -= weights[num]
        weights.pop(num)
        max_profit += profit[num]
        profit.pop(num)
    elif weights[num] > weight:
        max_profit += round(((weight/weights[num]) * profit[num]), 2)
        robbery_loot.append(f"{weight}/{weights[num]}")
        weight -= weight
        weights.pop(num)
     
print(f"The robber goes with a {robbery_loot[0]}kg, {robbery_loot[1]}kg, {robbery_loot[2]}kg gold pellets and makes ${max_profit} profit")

