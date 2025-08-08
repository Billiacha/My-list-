
my_list = []  # Create an empty list
my_list.append(10)  # Append 10
my_list.append(20)  # App20
my_list.append(30)  # Append 30
my_list.append(40)  # Append 40

my_list.insert(1, 15)  # Insert 15 at index 1

my_list.extend([50, 60, 70])  # Extend the list with [50, 60, 70]
my_list.pop()  # Remove the last element
my_list.sort()  # Sort the list in ascending order
index_30 = my_list.index(30)  # Find the index of the value 30
print("my_list:", my_list)
print("Index of 30:", index_30)
