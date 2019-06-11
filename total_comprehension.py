# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# Iteration
# 
# mapping_numbers = []
# 
# for i in my_numbers:
#   mapping_numbers.append(i * 100)
# 
# my_numbers #> [1, 2, 3, 4]
# mapping_numbers #> [100, 200, 300, 400]
#
# print("--------------")
# print("MAPPED LIST:", mapping_numbers)

#
# Mapping
#
# Option 1

# def enlarge(num):
#     return num * 100
# 
# MAPPING_LIST = map(enlarge, my_numbers)
# MAPPING_LIST #> <map object at 0x10c62e710>
# MAPPED_LIST = list(MAPPING_LIST) #> [100, 200, 300, 400]
# 

#
# Option 2
# 

MAPPED_LIST = [i * 100 for i in my_numbers] #> [100, 200, 300, 400]

print("--------------")
print("MAPPED LIST:", MAPPED_LIST)



# 
## Filtering
# 
# Option 1
# 

Filtered_list = list(filter(lambda i: i > 3, my_numbers))

# 
# Option 2
# 
# 
# def greater_than_three(i):
#     return i > 3
# Filtered_list = list(filter(greater_than_three, my_numbers))




print("--------------")
print("FILTERED LIST W/ MATCHES:", Filtered_list)




#
# Option 1
# 

Filtered_list_2 = list(filter(lambda i: i > 8, my_numbers))

# 
# Option 2
# 
#
# def greater_than_eight(i):
#     return i > 8
# Filtered_list = list(filter(greater_than_eight, my_numbers))


print("--------------")
print("FILTERED LIST W/O MATCHES:", Filtered_list_2)



## Mapping AND Filtering
# 
# MAPPED_LIST = [i * 100 for i in my_numbers]
# 
# Filtered_list_3 = list(filter(lambda i: i > 3*100, MAPPED_LIST))
# 
# print("--------------")
# print("MAPPED AND FILTERED LIST:", Filtered_list_3)
# 

## Filtering AND Mapping 

# Filtered_list = list(filter(lambda i: i > 3, my_numbers))
# 
# MAPPED_LIST_2 = [i * 100 for i in Filtered_list]
# 
# print("--------------")
# print("MAPPED AND FILTERED LIST:", MAPPED_LIST_2)
# 

## Option 3

last_list = [i * 100 for i in my_numbers if i > 3]

print("--------------")
print("MAPPED AND FILTERED LIST:", last_list)