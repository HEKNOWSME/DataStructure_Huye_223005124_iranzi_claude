import math
from array import array
# Practical Exercises for Arrays
# one dimension
# question 1
temperature_readings = array('f',[32.6, 35.5, 30.4, 25.7, 40.4, 30.6, 30.9])
for day, temperature in enumerate(temperature_readings):
     print(f"day {day + 1} had temperature {temperature}")
# question 2
def average(daily_sales):
     sum = 0
     days_of_week = 7
     for sale in daily_sales:
          sum += sale
     return math.floor(sum/ days_of_week)

daily_sales = [500, 300, 200, 100, 600, 1800, 600]
print(average(daily_sales))
# question 3
stock_prices = [100.5, 107.3, 109.2, 111.1, 109.4, 107.0, 106.9]
print(min(stock_prices))
print(max(stock_prices))

# question 4
student_marks_in_subject = [20, 50, 90, 80, 30, 90] # one subject with deferent student`s marks
reverse = student_marks_in_subject[::-1]
print(reverse)

# even number and odd number 
numbers = [1,3,5,7,6,7,10,4,8,10,12]
def countEven(numbers):
     count = 0
     for number in numbers:
          if number % 2 ==0:
               count += 1
     return count
print(countEven(numbers))

countOdd = len(numbers) - countEven(numbers)
print(countOdd)

# tic tac toe board
board = [
     ["x", "o", "x"], # row 1
     ["o", "o", "o"], # row 2
     ["o", "o", "x"], # row 3
]
def check_winner(board): 
     for row in board:
          if row[0] == row[1] == row[2]:
               return row[0] 
     for col in range(3):
          if board[0][col] == board[1][col] == board[2][col]:
               return board[0][col]
     if board[0][0] == board[1][1] == board[2][2]:
          return board[0][0]
     return "Toe"
print(check_winner(board))
sales = [
    [100, 150, 200, 250, 300, 350, 400], # product 1
    [120, 130, 140, 160, 180, 200, 220], # product 2
    [90, 110, 140, 170, 190, 210, 230],  # product 3
]

for i, product_sales in enumerate(sales):
    print(f"Sales for Product {i+1}: {product_sales}")

# RGB image invert
image = [
     [255, 0, 0], # red
     [0, 255, 0], # green
     [0, 0, 255], # blue
]
def invert_image(img):
     for row in img:
          row[0] = 255 - row[0]
          row[1] = 255 - row[1]
          row[2] = 255 - row[2]
     return img
print(invert_image(image))      

# total
marks = [
    [85, 90, 80],  # Student 1: Math, English, Science
    [78, 85, 88],  # Student 2: Math, English, Science
    [92, 87, 85]   # Student 3: Math, English, Science
]

for student, student_marks in enumerate(marks):
    total = sum(student_marks)
    print(f"Total marks for Student {student+1}: {total}")

temperatures = [
    #m #tue #wen #thu #fri #sat #san
    [30, 32, 29, 10, 12, 15, 14],# City 1
    [25, 26, 24, 30, 32, 29, 23], # City 2
    [15, 16, 14, 25, 26, 24, 20], # City 3
    [10, 12, 9, 15, 16, 14, 30]   # City 4
]
for index, city in enumerate(temperatures):
     arg = math.floor(sum(city) / 7)
     print(f"the average temperature of the city {index+1} is {arg}")
        
# Practical Exercises for Lists
# 1
attendees = ['name 1', 'name 2', 'name 4']
attendees.append('name added')
print(attendees)
# 2
shopping_list = ['milk', 'eggs', 'Butter']
shopping_list.remove('eggs')
print(shopping_list)

# 3
ages = [34, 21, 45, 19, 23]
ages.sort()
print(ages)

# 4
to_do_list = ['Task 1', 'Task 2', 'Task 3']
completed_task = to_do_list.pop(1)
print(f"Completed: {completed_task}")
print(f"Remaining tasks: {to_do_list}")
# 
friends1 = ['Alice', 'Bob', 'Charlie']
friends2 = ['David', 'Charlie', 'Edward']

# Multi-Dimensional Lists:
students = [
     ['alice', 12, "A"],
     ['bob', 20, "C"],
     ['charles', 18, "B"]
]
students.sort(key=lambda student: student[2])
print(students)

