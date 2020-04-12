def binary_search(arr, val):
    if len(arr)==0 or len(arr)==1 and arr[0] != val:
        return False
    arr.sort()
    mid = arr[len(arr)//2]

    if mid == val:
        return True
    if val<mid: return binary_search(arr[:len(arr)//2], val)
    if val>mid: return binary_search(arr[len(arr)//2:], val)
