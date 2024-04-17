N, M = map(int, input().split())
N_list = list(map(int, input().split()))
tmp = 0
tmp_val = []
for i in range(N - M + 1):
    tmp_val.append(sum(N_list[i:i+M]))
print(max(tmp_val))