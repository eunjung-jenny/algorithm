# 퀵 정렬
## 재귀 알고리즘과 pivot 이라는 개념을 활용하여
## pivot?
### 1. Correct position in final, sorted array
### 2. Items to the left are smaller
### 3. Items to the right are larger
## How to select pivot?
### median of three : 첫 번째, 가운데, 마지막 원소를 정렬한 뒤 가운데 값을 pivot으로 설정
## Concept
### pivot을 마지막으로 보낸 뒤, 제일 왼쪽에서부터 pivot보다 큰 값의 인덱스, 제일 오른쪽에서부터 pivot보다 작은 값의 인덱스를 구하여 큰 값의 인덱스가 작은 값의 인덱스보다 커지기 전까지(종료 조건) 둘을 swap 하는 과정을 반복. 종료 조건에 도달하면 pivot보다 큰 값의 인덱스와 pivot을 swap 하는 과정을 반복하는 방법

from random import shuffle

def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array)//2]
    less, greater = [], []

    for elem in array:
        if elem < pivot:
            less.append(elem)
        elif elem > pivot:
            greater.append(elem)

    sorted = quickSort(less) + [pivot] + quickSort(greater)    
    print(sorted)
    return sorted

lst = list(range(1, 13))
shuffle(lst)
print(lst)

quickSort(lst)