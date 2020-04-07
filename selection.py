# 선택 정렬
## 전체에서 가장 작은 수를 찾아서 제일 앞에서부터 차례대로 swap 해가며 채워나간다.

from random import shuffle

lst = list(range(1, 13))
shuffle(lst)

for i in range(len(lst)):
    minimum = lst[i]
    minimim_idx = i
    for j in range(i+1, len(lst)):
        if lst[j] < minimum:
            minimum = lst[j]
            minimum_idx = j

    lst[i], lst[minimum_idx] = lst[minimum_idx], lst[i]



