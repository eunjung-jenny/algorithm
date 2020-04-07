# 병합 정렬
## 재귀 알고리즘, divide & conquer 방식을 활용하여 자료를 가장 작은 단위로 쪼갠 뒤 이를 다시 합치며 정렬하는 방법

from random import shuffle

def merge(arr_a, arr_b):
    arr = []
    i, j = 0, 0
    
    while ((i < len(arr_a)) and (j < len(arr_b))):
        if arr_a[i] < arr_b[j]:
            arr.append(arr_a[i])
            i += 1
        else:
            arr.append(arr_b[j])
            j += 1
    
    if i < len(arr_a):
        arr.extend(arr_a[i:])
    if j < len(arr_b):
        arr.extend(arr_b[j:])
    
    return arr
        

def mergeSort(array):
    if len(array) == 1:
        return array
    
    half = len(array)//2
    array_one = mergeSort(array[:half])
    array_two = mergeSort(array[half:])
    
    merged = merge(array_one, array_two)
    print(merged)
    return merged



lst = list(range(1, 13))
shuffle(lst)
print(lst)

mergeSort(lst)
