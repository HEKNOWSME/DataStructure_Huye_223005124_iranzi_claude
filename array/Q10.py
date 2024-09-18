import math
temperatures = [
    #m #tue #wen #thu #fri #sat #san
    [30, 32, 29, 10, 12, 15, 14],# City 1
    [25, 26, 24, 30, 32, 29, 23], # City 2
    [15, 16, 14, 25, 26, 24, 20], # City 3
    [10, 12, 9, 15, 16, 14, 30]   # City 4
]
for index, city in enumerate(temperatures):
     arg = round(sum(city) / len(city))
     print(f"the average temperature of the city {index+1} is {arg}")
        