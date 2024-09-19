expenses = [
    [1000, 1200, 1100, 2500, 200, 100],
    [300, 350, 320, 1000, 1200, 300],     
    [200, 250, 220, 360, 400, 200]      
]

for index, category in enumerate(expenses):
    average = sum(category) / 6
    print(f"Average expense for category {index+1}: is {round(average)}")