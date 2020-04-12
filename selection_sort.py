from random import randint

def create_array(length=10, maxint=50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr

def selection_sort(A):
    for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
        A[i], A[min_idx] = A[min_idx], A[i]

    
##    sort_len = 0
##    while sort_len<len(a):
##        min_idx = None
##        for i, elem in enumerate(a[sort_len:]):
##            if min_idx == None or elem<a[min_idx]:
##                print("min_idx",min_idx)
##                print("sort_len",sort_len)
##                print("i",i)
##                min_idx = i+sort_len
##                print("a[sort_len]", a[sort_len])
##                print("a[min_idx]", a[min_idx])
##        a[sort_len], a[min_idx] = a[min_idx],a[sort_len]
##        sort_len += 1
##        print("new sort_len",sort_len)
    return A


