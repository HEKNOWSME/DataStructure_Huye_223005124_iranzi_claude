rgb_image = [
       [0, 0, 255], # Red 
       [0, 255, 0 ], # green
       [0, 0, 255]   # blue
       ] 
def rgb_image_invert_colors(colors):
       for color in colors:
              color[0] = 255 -color[0]
              color[1] = 255 -color[1]
              color[2] = 255 -color[2]
       return colors
print(rgb_image_invert_colors(rgb_image))

sales = [
    [100, 150, 200, 250, 300, 350, 400], 
    [120, 130, 140, 160, 180, 200, 220],  
    [90, 110, 140, 170, 190, 210, 230],   
]

for day, product_sales in enumerate(sales):
    print(f"Sales for Product {day+1}: {product_sales}")