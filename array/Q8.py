
image = [
     [255, 0, 0], # red
     [0, 255, 0], # green
     [0, 0, 255], # blue
]
for row in image:
       row[0] = 255 - row[0]
       row[1] = 255 - row[1]
       row[2] = 255 - row[2]
print(image)