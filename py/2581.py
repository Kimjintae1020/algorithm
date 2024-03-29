start_num = int(input())
last_num = int(input())

so_list = []


for num in range(start_num,last_num+1):
    count = 0
    if num > 1:
        for i in range(2,num):  # 2 ~ num-1 까지

            if num %  i == 0:
                count = count + 1
                break


            # 소수리스트 추가 
        if count == 0:
                so_list.append(num)


if len(so_list) > 0:
    print(sum(so_list))
    print(min(so_list))
else:
    print(-1)