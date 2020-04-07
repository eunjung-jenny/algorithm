# 삽입 정렬
## 제일 앞에서부터 그 앞 숫자와 값을 비교하고 결과에 따라 swap 하는 과정을 반복하여 제자리에 삽입하는 방식

from random import shuffle

lst = list(range(1, 13))
shuffle(lst)
print(lst)

for i in range(len(lst)):
    curr = i
    while curr > 0:
        comp = curr-1
        if lst[comp] > lst[curr]:
            lst[curr], lst[comp] = lst[comp], lst[curr]
            print(lst)
            curr = comp
        else:
            break
    
print(lst)