'''
점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.
김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.
사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.

출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.
방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.

한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.

입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.

총 10개의 테스트 케이스가 주어진다.
'''

import sys
sys.stdin = open("input_ladder.txt", "r")

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
n = 10
for _ in range(11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    for j in range(l):
        i = 99
        k = j
        if ladder[i][k] == 2:
            while i > 0:
                ladder, i, k = deltasearch(ladder, i, k)
            print(f'#{t} {k}')