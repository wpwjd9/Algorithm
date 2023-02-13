'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

1. N 은 5 이상 15 이하이다.

2. M은 2 이상 N 이하이다.

3. 각 영역의 파리 갯수는 30 이하 이다.

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,

다음 N 줄에 걸쳐 N x N 배열이 주어진다.

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]
    max_kills = 0
    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            kills = 0
            for fi in range(m):
                for fj in range(m):
                    kills += flies[i + fi][j + fj]
            if kills >= max_kills:
                max_kills = kills

    print(f'#{t} {max_kills}')