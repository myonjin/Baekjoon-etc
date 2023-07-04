import sys
from collections import defaultdict

for _ in range(int(input())):
    word = sys.stdin.readline().rstrip()
    k = int(input())
    dic_cnt = defaultdict(list)
    for i,ch in enumerate(word):
        if word.count(ch) >= k:
            dic_cnt[ch].append(i)
    min_len = 10002
    max_len = 0
    for ch,ch_idx_list in dic_cnt.items():
        start = 0
        end = start + k - 1
        while end < len(ch_idx_list):
            length = ch_idx_list[end] - ch_idx_list[start] + 1
            if length < min_len:
                min_len = length
            if length > max_len:
                max_len = length
            start += 1
            end = start + k - 1
    if min_len == 10002:
        print(-1)
    else:
        print(min_len,max_len)

