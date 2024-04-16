import sys
input = sys.stdin.readline

n = int(input())    # 재료의 개수 n
m = int(input())    # 갑옷을 만드는 필요한 수

num_li = list(map(int,input().split()))
cnt = 0
# 2개의 재료는 -> m이 되어야함

num_li.sort()
#투 포인터
left = 0
right = len(num_li) - 1


while left < right:
    sum_num = num_li[left] + num_li[right]

    if sum_num < m:
        left += 1

    elif sum_num > m:
        right -= 1

    else:
        cnt += 1
        left += 1
        right -= 1


print(cnt)