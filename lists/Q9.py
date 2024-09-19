stock_product = [
       ['Meat', 500, 18], 
       ['Milk', 400, 0], 
       ['Eggs', 600, 18],
       ['Potatoes', 300, 0],
       ]
out_of_stock = [product for product in stock_product if product[2] == 0]
out_of_stock_product_names = [product[0] for product in stock_product if product[2] == 0]
available_products = [product for product in stock_product if product[2] > 0]
print(out_of_stock)
print( "products out of the stock are", out_of_stock_product_names)
print("available products are", available_products)