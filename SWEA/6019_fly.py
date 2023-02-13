'''

'''

T = int(input())
for t in range(1, T + 1):
    d, a, b, fly = list(map(int, input().split()))







    ans = (d / (a + b)) * fly

    print(f'#{t} {ans}')