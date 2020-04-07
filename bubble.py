# 버블 정렬
## 제일 앞에서부터 바로 뒤의 숫자와 값을 비교, swap 하는 과정을 반복하여 가장 큰 숫자를 뒤에서부터 채워나가는 방법 

from random import shuffle

lst = list(range(1, 13))
shuffle(lst)
print(lst)

for i in range(len(lst)):
    curr = 0
    for _ in range(len(lst) - 1 - i):
        if lst[curr] > lst[curr+1]:
            lst[curr], lst[curr+1] = lst[curr+1], lst[curr]
            print(lst)
        curr += 1
        

print(lst)
