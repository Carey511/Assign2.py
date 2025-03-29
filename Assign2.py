# 1. Create an empty list

my_list = []
print(my_list)

# 2. Appending: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
# 3. Insert the value 15 
my_list.insert(1, 15)
print(my_list)

# 4. Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

# 5. Remove the last element from my_list
my_list.pop()
print(my_list)

# 6. Sort my_list in ascending order
my_list.sort()
print(my_list)

# 7. Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(index_of_30)
