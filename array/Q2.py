daily_sales = [500, 300, 200, 100, 600, 1800, 600]
sum = 0
for sale in daily_sales:
       sum += sale

average = round((sum / len(daily_sales))
)
print(average)