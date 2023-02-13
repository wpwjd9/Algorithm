'''
0에서 9까지 숫자가 적힌 n장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트 케이스의 첫 줄에 카드 장수 n이 주어진다.
다음 줄에 n개의 숫자 a[i]가 여백없이 주어진다.(0으로 시작할 수도 있다.)

각 줄마다 "#T"를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

3
5
49679
5
08271
10
7797946543
'''

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input()))
    counts = [0] * 10
    for i in arr:
        counts[i] += 1
    print(counts)
    max_count = counts[0]
    max_num = 0
    for j in range(len(counts)):
        if counts[j] > max_count:
            max_count = counts[j]
            max_num = j
        elif counts[j] == max_count:
            max_num = j
    print(f'#{t} {max_num} {max_count}')