import sys
sys.stdin = open("input_ladder2.txt", "r")

import copy

def deltasearch(arr, i, j):
    if 0 < j < 99:
        if arr[i][j - 1] == 0 and arr[i][j + 1] == 0:
            arr[i][j] = 0
            i -= 1
            return arr, i, j
        elif arr[i][j - 1] == 1:
            arr[i][j] = 0
            j -= 1
            return arr, i, j
        elif arr[i][j + 1] == 1:
            arr[i][j] = 0
            j += 1
            return arr, i, j
    elif j == 0:
        if arr[i][j + 1] == 0:
            arr[i][j] = 0
            i -= 1
            return arr, i, j
        else:
            arr[i][j] = 0
            j += 1
            return arr, i, j
    elif j == 99:
        if arr[i][j - 1] == 0:
            arr[i][j] = 0
            i -= 1
            return arr, i, j
        else:
            arr[i][j] = 0
            j -= 1
            return arr, i, j


l = 100
for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 9999
    min_cnt_idx = 0
    for j in range(l):
        i = 99
        k = j
        cnt = 0
        ladder_t = copy.deepcopy(ladder)
        if ladder[i][k] == 1:
            while i > 0:
                ladder_t, i, k = deltasearch(ladder_t, i, k)
                cnt += 1
            if min_cnt >= cnt:
                min_cnt = cnt
                min_cnt_idx = k
    print(f'#{t} {min_cnt_idx}')
