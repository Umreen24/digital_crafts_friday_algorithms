

my_array = [1,2,3,4,5]
new_array = []

#using for loop
for x in my_array:
    if x in my_array:
        new_array.append(x)
    
    
for x in my_array:
    if x in my_array:
        new_array.append(x)
    
print(new_array)


# using function
def new_array_2(my_array):
    return my_array + my_array

new = new_array_2(my_array)
print(new)

print(my_array + my_array)

