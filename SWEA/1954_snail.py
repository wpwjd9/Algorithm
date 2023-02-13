'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.
'''

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    x, y = 0, 0
    direction = 0
    for i in range(1, n**2 + 1):
        snail[x][y] = i
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= n or y >= n or snail[x][y] != 0:
            x -= dx[direction]
            y -= dy[direction]

            direction = (direction + 1) % 4

            x += dx[direction]
            y += dy[direction]

    print(f'#{t}')
    for x in snail:
        print(*x)
    print()
