# n = int(input())
# count = n

# for i in range(n):
#     word = input()

#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] == word[j+1]:
#             count = count - 1
#             break
        
# print(count)

n = int(input())

cnt = n

for _ in range(n):
    word = input()
    for i in range(len(word) -1):
        if word[i] != word[i+1]:
            if word[i+1] in word[:i]:
                cnt -= 1
                
                break
print(cnt)