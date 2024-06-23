import sys
input = sys.stdin.readline

a = int(input())

li_num = []

for i in range(a):
    x, y  = map(int,input().split())
    li_num.append([y, x])


s_num = sorted(li_num)    

for y,x in s_num:
    print(x,y)