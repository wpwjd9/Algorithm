'''
다음 100x100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하시오.

총 1개의 테스트 케이스가 주어진다.
배열의 크기는 100x100으로 동일하다.
각 행의 합은 integer 범위를 넘어가지 않는다.
동일한 최댓값이 잇을 경우, 하나의 값만 출력한다.
'''

for x in range(10):
    t = int(input())
    n = 100                                                     # 행과 열의 크기
    arr = [list(map(int, input().split())) for _ in range(n)]   # n개 행의 데이터를 저장하는 2차원 배열 arr
    row_sum_max = 0                                             # 행의 합들 중 가장 큰 값을 저장하기 위한 변수
    col_sum_max = 0                                             # 열의 합들 중 가장 큰 값을 저장하기 위한 변수
    dia_sum = 0                                                 # 오른쪽 아래로 향하는 대각선에 위치한 요소들의 합을 저장하기 위한 변수
    rev_dia_sum = 0                                             # 왼쪽 아래로 향하는 대각선에 위치한 요소들의 합을 저장하기 위한 변수
    # 모든 행에 대하여 합을 구하는 코드블럭
    for i in range(n):
        row_sum = 0
        for j in range(n):
            row_sum += arr[i][j]
        if row_sum >= row_sum_max:                               # 행의 합들 중 가장 큰 값을 가려내기 위한 if문
            row_sum_max = row_sum

    # 모든 열에 대하여 합을 구하는 코드블럭
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += arr[i][j]
        if col_sum >= col_sum_max:                               # 열의 합들 중 가장 큰 값을 가려내기 위한 if문
            col_sum_max = col_sum

    # 대각선의 합을 구하는 코드블럭
    for i in range(n):
        for j in range(n):
            if i == j:
                dia_sum += arr[i][j]

    # 반대 방향의 대각선의 합을 구하는 코드블럭
    for i in range(n):
        for j in range(-1, -n + 1, -1):
            if i + (n + 1) + j == n:
                rev_dia_sum += arr[i][j]

    # 4개의 값들 중 가장 큰 값만을 출력한다.
    print(f'#{t} {max(row_sum_max, col_sum_max, dia_sum, rev_dia_sum)}')