from random import randint

def create_array(len = 10, max=50):
    new_arr = [randint(0,max) for _ in range(len)]
    return new_arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j= i-1

        while j >=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr
