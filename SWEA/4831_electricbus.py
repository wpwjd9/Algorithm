'''
A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

첫 줄에 노선 수 T가 주어진다.
각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다.

4
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17
5 100 20
6 10 15 20 25 30 35 40 45 50 55 60 65 70 75 76 81 85 90 95
'''

T = int(input())
for t in range(1, T + 1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    charger_loc = [0] * (n+ k)
    for i in arr:
        charger_loc[i] += 1

    bus = 0
    c_count = 0
    while bus < n:
        if bus + k > n:
            break
        last_charge = 0
        for j in range(1, k + 1):
            if charger_loc[bus + j]:
                last_charge = bus + j
            if last_charge + k >= n or bus + j >= n:
                break
        if last_charge:
            c_count += 1
        else:
            c_count = 0
            break
        bus += k

    print(f'#{t} {c_count}')