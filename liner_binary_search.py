def linear_search(list, item):
    for n in range(len(list)):
        if list[n] == item:
            return n
    return None

# array = [10,20,30,40,50]
# print(linear_search(array,40))



def binary_search(list, item ):
    low = 0
    high =len(list)-1 
    while low <=high:
        mid = (low + high)//2
        guess =list[mid]
        if guess == item:
            return mid 
        if guess > item :
            high = mid -1
        else:
            low = mid +1

    return None        

array = [10,60,30,15,50]
array.sort()
print(array)
print(linear_search(array,15))
print(binary_search(array,15))