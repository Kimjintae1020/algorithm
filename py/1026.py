n = int(input())

a_li = list(map(int,input().split()))
b_li = list(map(int,input().split()))

sorted_a = sorted(a_li,reverse = True)     #내림차순 정렬
sorted_b = sorted(b_li)                    #오름차순 정렬


sum = 0
for i in range(n): 
    sum += sorted_a[i] * sorted_b[i]

print(sum)