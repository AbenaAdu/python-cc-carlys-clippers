hairstyles = [
              "bouffant", 
              "pixie", 
              "dreadlocks", 
              "crew", 
              "bowl", 
              "bob", 
              "mohawk", 
              "flattop"
              ]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Add all the prices 
total_price = 0
for price in prices:
  total_price += price

#Average price of prices
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

#New Prices 
new_prices = [price - 5 for price in prices]

#This loop generates the total revenue for the week based on prices and how many people did a style
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i]) 
  
print("Total Revenue: " + str(total_revenue))

#Average daily revenue
average_daily_revenue = total_revenue / 7

#New List that lists cuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]