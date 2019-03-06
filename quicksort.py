#coding=utf-8

def quick_sort(arr, start, end):
    '''
    快排递归程序
    '''
    if start < end:
        key = divide(arr, start, end)
        quick_sort(arr, start, key-1)
        quick_sort(arr, key+1, end)


def divide(arr, start, end):
    '''
    定位基准点，切分array为大小两半
    '''
    key = start 
    arr[key] = arr[key]
    while start < end:
        while start<end and arr[key]<=arr[end]:
            end -= 1
        while start<end and arr[key]>=arr[start]:
            start += 1  
        arr[start], arr[end] = arr[end], arr[start]
    arr[key], arr[start] = arr[start], arr[key]
    assert start==end
    key = start
    return key

            
#@test
if __name__ == "__main__":
    
    arr = [1,2,7,9,3,4,5,10,8]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)