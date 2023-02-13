'''
"기러기", "토마토", "스위스"와 같이 똑바로 읽어도 거꾸로 읽어도 똑같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.

각 칸의 들어가는 글자는 'A', 'B', 'C' 중 하나이다.

ABA도 회문이며, ABBA도 회문이다. A 또한 길이 1짜리 회문이다.

가로 또는 세로로 이어진 회문의 개수만 센다.

총 10개의 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.
'''

def palindrome_h(arr, n, m):                        # 가로 방향 탐색
    cnt = 0                                         # 회문이 있을 때마다 count 해주기 위한 변수
    for i in range(n):                              # 모든 행에 대하여
        y = 0
        while y <= n - m:                           # m만큼 탐색할 수 있는 인덱스까지의 y값 설정
            p = []                                  # 각 문자를 담을 빈 리스트
            for j in range(m):                      # m번 만큼 반복
                p.append(arr[i][y + j])
            y += 1                                  # 한 행에 대해서 가능한 모든 탐색을 마치면 y + 1
            if ''.join(p) == ''.join(p[::-1]):      # 그렇게 담긴 문자들을 문자열로 묶어 정방향 역방향으로 비교하여
                cnt += 1                            # 일치한다면 cnt + 1
    return cnt                                      # cnt 반환

def palindrome_v(arr, n, m):                        # 세로 방향 탐색
    cnt = 0
    for j in range(n):                              # 모든 열에 대하여
        x = 0
        while x <= n - m:                           # m만큼 탐색할 수 있는 인덱스까지의 x값 설정
            p = []
            for i in range(m):
                p.append(arr[x + i][j])
            x += 1                                  # 한 열에 대해서 가능한 모든 탐색을 마치면 x + 1
            if ''.join(p) == ''.join(p[::-1]):
                cnt += 1
    return cnt

# T = int(input())
T = 10
for t in range(1, T + 1):
    n = 8
    m = int(input())
    arr = [list((input())) for _ in range(n)]
    print(f'#{t} {palindrome_v(arr, n, m) + palindrome_h(arr, n, m)}')  # 가로로 탐색한 결과와 세로로 탐색한 결과를 더하여 테스트 케이스와 함께 출력