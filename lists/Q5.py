friends1 = ['Alice', 'Bob', 'Charlie', 'Edward']
friends2 = ['David', 'Charlie', 'Edward']
for friend in friends1:
       if friend in friends2:
              friends2.remove(friend)
       combined = friends1 + friends2
print(combined) 
# or using set
combined_friends = list(set(friends1 + friends2))
print(combined_friends)                              