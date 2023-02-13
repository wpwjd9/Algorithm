'''
n개의 정수가 들어있는 배열에서 이웃한 m개의 합을 계산하는 것은 디지털 필터링의 기초연산이다.
m개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.

첫 줄에 테스트 케이스 개수 T가 주어진다. ( 1 =< T =< 50)
다음 줄부터 테스트 케이스의 첫 줄에 정수의 개수 n과 구간의 개수 m이 주어진다. (10 =< n =< 100, 2 =< m < n)
다음 줄에 n개의 정수 a(i)가 주어진다. (1 =< a(i) =< 1000000)

각 줄마다 "#T"(테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
'''

T = int(input())    # 테스트 케이스의 수를 입력받는다.
for t in range(1, T + 1):   # 테스트 케이스의 수만큼 반복하는 반복문
    n, m = map(int, input().split())    # n과 m을 함께받아 split으로 나누어 각각 저장한다. n은 정수의 개수, m은 구간의 개수이다.
    arr = list(map(int, input().split()))   # n개의 양수를 입력받는다.
    max_sum = 0 # 비교를 위한 max_sum
    min_sum = 10000000  # 비교를 위한 min_sum, 결국엔 구간의 합이 가장 작았을 때의 그 합을 담을 것이기 때문에 0이 아닌 큰 숫자로 초기화한다.
    for i in range(0, n - m + 1):   # 0번째 인덱스부터 시작하고 총 양수의 개수에서 구간의 크기를 뺀 것에 1을 더한 것까지 범위를 설정한다.
        num_sum = 0 # 구간의 합을 담기 위한 num_sum
        for j in range(m):  # 구간의 크기(횟수)만큼 반복해주는 반복문
            num_sum += arr[i+j] # 인덱스를 1씩 구간의 크기(횟수)만큼 증가시키고 num_sum에 누적한다.
        if max_sum < num_sum:   # 위에서 설정해둔 max_sum보다 num_sum이 크다면
            max_sum = num_sum   # max_sum의 값을 num_sum으로 바꿔준다.
        if min_sum > num_sum:   # 위에서 설정해둔 min_sum보다 num_sum이 작다면
            min_sum = num_sum   # min_sum의 값을 num_sum으로 바꿔준다.
    print(f'#{t} {max_sum - min_sum}')  # 마지막으로 테스트 케이스 번호와 구간의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력한다.

#1 21
#2 11088
#3 1090