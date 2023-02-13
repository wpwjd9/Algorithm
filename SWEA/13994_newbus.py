'''


'''

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    counts = [0] * 1001
    for j in range(n):
        bus_info = list(map(int, input().split()))
        counts[bus_info[1]] += 1
        counts[bus_info[2]] += 1
        if bus_info[0] == 1:
            for a in range(bus_info[1] + 1, bus_info[2]):
                counts[a] += 1

        elif bus_info[0] == 2:
            for a in range(bus_info[1] + 2, bus_info[2], 2):
                counts[a] += 1

        elif bus_info[0] == 3 and (bus_info[1] % 2) == 0:
            for a in range(bus_info[1] + 1, bus_info[2]):
                if a % 4 == 0:
                    counts[a] += 1

        elif bus_info[0] == 3 and (bus_info[1] % 2) == 1:
            for a in range(bus_info[1] + 1, bus_info[2]):
                if a % 3 == 0 and a % 10 != 0:
                    counts[a] += 1

    print(f'#{t} {max(counts)}')