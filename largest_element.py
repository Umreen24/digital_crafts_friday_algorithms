
my_array = [1000, 220, 34, 54, 88, 90, 330, 10, 50120, 777899]
n = len(my_array)

def largest_number(my_array,n):

    max_number = my_array[0]

    for x in range(1,n):
        if my_array[x] > max_number:
            max_number = my_array[x]
    return max_number


answer = largest_number(my_array,n)

print(answer)
#print([my_array[0]])
