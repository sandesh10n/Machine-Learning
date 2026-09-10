
# List should be included in the square brackets

my_list = [1, 2, 3, 4]
print(my_list)
print(type(my_list))

# lists can have multiple data types

my_list = [2, 3.4, 'English', True]
print(my_list)

# list are mutables

# add elements to  the list

my_list.append(6)
print(my_list)

print(my_list[0])

# List allows duplicate values
list_1 = [1,2,3,42,2,3]
print(list_1)

print(len(list_1))

list_2 = []
print(list_2)

list_2.append(5)
print(list_2)

del list_1[1]
print(list_1)

list_3 = [1,2,3,4,5]
list_4 = [6,7,8,9,10]
list_5 = list_3 + list_4
print(list_5)

#Tuple

#Tuple are immutable
tuple_1 = (2, 3, 4, 5)
print(tuple_1)
print(type(tuple_1))

#tuple allow multiple data types in single tuple
tuple_2 = (1, 2, 3.5, "Machine learning", False)
print(tuple_2)

# Converting list into the tuple 
my_list = [3,4,5,6]
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

print(my_tuple[0])
print(my_tuple[1])

# Tuples are immutable ---> Unchangeable
#my_tuple.append(6)

print(len(my_tuple))

# Set
# Set ---> Enclosed in curly brackets
my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

#print(my_set[0])

# Convert list to the set
list_6 = [4,5,6,7]
set_6 = set(list_6)
print(type(set_6))

# Set doesn't allow duplicate values
set_3 = {1,2,3,4,5,1,2,3}
print(set_3)


# Dictionary
# Key-Value pair

my_dictionary = {'name' : 'David', 'age' : 32, 'country' : "America"}
print(my_dictionary)
type(my_dictionary)

print(my_dictionary['name'])
print(my_dictionary['age'])
print(my_dictionary['country'])

# Dictinary doesn't allow duplicate values

dictionary_2 = {'name' : 'David', 'age' : 32, 'country' : "America", 'name' : 'David', 'age' : 32, 'country' : "America"}
print(dictionary_2)


