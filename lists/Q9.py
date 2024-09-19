stock_product = [
       ['product 1', 500, 18], 
       ['product 2', 400, 0], 
       ['product 3', 600, 18],
       ['product 4', 300, 0],
       ]
out_of_stock = [product for product in stock_product if product[2] == 0]
out_of_stock_product_names = [product[0] for product in stock_product if product[2] == 0]
print(out_of_stock)
print(out_of_stock_product_names)