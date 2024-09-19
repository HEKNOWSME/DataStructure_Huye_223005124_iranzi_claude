sales = [
    [100, 150, 200, 250, 300, 350, 400], 
    [120, 130, 140, 160, 180, 200, 220],  
    [90, 110, 140, 170, 190, 210, 230],   
]

for day, product_sales in enumerate(sales):
    print(f"Sales for Product {day+1}: {product_sales}")