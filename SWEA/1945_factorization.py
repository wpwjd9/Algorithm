'''
10
6791400
1646400
1425600
8575
185625
6480
1185408
6561
25
330750
'''

divs = [2, 3, 5, 7, 11]
T = int(input())
for t in range(1, T + 1):
    n = int(input())
    counts = [0] * len(divs)    # 소수의 개수만큼의 빈 리스트 생성(해당 소수로 몇 번 나누어졌는지 count하기 위함)

    for i in range(len(divs)):
        while n % divs[i] == 0: # 해당 소수로 n을 나누었을때 나머지 없이 나누어 떨어질때까지 반복
            counts[i] += 1      # 해당 수로 나누어 졌다는 뜻이므로 counts + 1
            n = n // divs[i]    # 몫만을 가져와 반복문 다시 실행

    print(f'#{t}', *counts)