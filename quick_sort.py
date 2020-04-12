from random import randint
def create_array(len=10, max=50):
    return [randint(0,max) for _ in range(len)]

def quick_sort(arr):
    if len(arr) <=1: return arr

    pivot = arr[randint(0,len(arr)-1)]
    
    smaller, equal, larger = [],[],[]

    for x in arr:
        if x<pivot: smaller.append(x)
        elif x==pivot: equal.append(x)
        else: larger.append(x)

    return quick_sort(smaller)+equal+quick_sort(larger)
