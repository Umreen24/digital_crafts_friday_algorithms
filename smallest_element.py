

my_array = [1000, 220, 34, 54, 88, 90, 330, 10, 50120, 777899]
n = len(my_array)

def smallest_number(my_array,n):

    min_number = my_array[0]

    for x in range(1,n):
        if my_array[x] < min_number:
            min_number = my_array[x]
    return min_number


answer = smallest_number(my_array,n)

print(answer)

#print(n)
