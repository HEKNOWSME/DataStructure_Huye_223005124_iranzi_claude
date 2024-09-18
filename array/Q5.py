numbers = [1,3,5,7,6,7,10,4,8,10,12]
count = 0
for number in numbers:
       if number % 2 ==0:
              count += 1


print(f" the number of even in numbers array is {count}")
countOdd = len(numbers) - count
print(f" the number of odd in numbers array is {countOdd}")