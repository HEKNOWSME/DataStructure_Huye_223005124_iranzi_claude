theater_seating = [
       ['seat 1', 'seat 2', "seat 3", 'seat 4'], 
       ['seat 5', 'seat 6', "reserved", 'seat 8'], 
       ['seat 9', 'seat 10', "seat 11", 'seat 12'], 
       ]
reserved = 'reserved'
for index, block in enumerate(theater_seating):
       for place, seat in enumerate(block):
              if seat == 'reserved':
                     print(f"the seat {place + 1} in block {index + 1} is reserved")