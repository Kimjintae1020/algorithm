a = int(input())
b = int(input())
c = int(input())

#  List'17037300' 로 묶음
ans = list(str(a * b * c))

for i in range(10):
    # i를 str로 변환해 count로 매칭되는 개수를 리턴
    print(ans.count(str(i)))
