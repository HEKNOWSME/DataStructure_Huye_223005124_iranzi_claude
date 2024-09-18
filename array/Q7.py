shop = [
    [100, 150, 200, 250, 300, 350, 400], # Cassavas
    [120, 130, 140, 160, 180, 200, 220], # Potatoes
    [90, 110, 140, 170, 190, 210, 230],  # Beans
]

for i, product_sales in enumerate(shop):
       if i ==0:
              i = "Cassavas"
       elif i == 1:
              i = "Potatoes"
       elif i == 2:
              i = "Beans"
       print(f"Sales for {i} over the week is {product_sales}")