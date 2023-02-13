'''
ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.

회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
'''

def palindrome_h(arr, n, m):                        # 가로 방향 탐색
    for i in range(n):                              # 모든 행에 대하여
        y = 0
        while y <= n - m:                           # m만큼 탐색할 수 있는 인덱스까지의 y값 설정
            p = []                                  # 각 문자를 담을 빈 리스트
            for j in range(m):                      # m번 만큼 반복
                p.append(arr[i][y + j])
            y += 1                                  # 한 행에 대해서 가능한 모든 탐색을 마치면 y + 1
            if ''.join(p) == ''.join(p[::-1]):      # 그렇게 담긴 문자들을 문자열로 묶어 정방향 역방향으로 비교하여
                return ''.join(p)                   # 같으면 해당 문자열 반환

def palindrome_v(arr, n, m):                        # 세로 방향 탐색
    for j in range(n):                              # 모든 열에 대하여
        x = 0
        while x <= n - m:                           # m만큼 탐색할 수 있는 인덱스까지의 x값 설정
            p = []
            for i in range(m):
                p.append(arr[x + i][j])
            x += 1                                  # 한 열에 대해서 가능한 모든 탐색을 마치면 x + 1
            if ''.join(p) == ''.join(p[::-1]):
                return ''.join(p)

T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list((input())) for _ in range(n)]
    if palindrome_h(arr, n, m):
        print(f'#{t} {palindrome_h(arr, n, m)}')    # 가로로 탐색하였을 때 반환값이 존재한다면 그 반환값 출력
    elif palindrome_v(arr, n, m):
        print(f'#{t} {palindrome_v(arr, n, m)}')    # 세로로 탐색하였을 때 반환값이 존재한다면 그 반환값 출력
