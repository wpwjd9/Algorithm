'''
보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.

N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100

3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
'''

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n - 1):
        min_idx = i
        max_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
            elif arr[max_idx] < arr[j]:
                max_idx = j
        if i % 2:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
    print(f'#{t}', *arr[:10])