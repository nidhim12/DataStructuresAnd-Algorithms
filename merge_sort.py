def create_array(len=10, max=50):
    from random import randint
    new_arr = [randint(0,max) for _ in range(len)]

    return new_arr


def merge(a, b):
    a_idx =0
    b_idx = 0
    c = []
    while a_idx<len(a) and b_idx<len(b):
        if a[a_idx]<b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a): c.extend(b[b_idx:])

    else: c.extend(a[a_idx:])

    return c

def merge_sort(arr):
    if len(arr)<= 1: return arr

    left, right = merge_sort(arr[: len(arr)//2]), merge_sort(arr[len(arr)//2 :])


    return merge(left, right)
        
