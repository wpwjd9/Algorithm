'''


'''

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    # n번 반복하면서 노선입력 ,빈도수 표시
    counts = [0] * 5001                             # 정류장의 수만큼 counts 리스트 생성
    for _ in range(n):
        start_p, end_p = map(int, input().split())  # 버스 노선의 시작점과 종점
        for i in range(start_p, end_p + 1):         # 버스가 지나가는 곳 마다 1을 추가해준다.
            counts[i] += 1

    P = int(input())                                # 몇 개의 버스 노선이 다니는지 체크하려는 정류장의 개수
    bus_count = []                                  # 해당 정류장에 몇 개의 노선이 지나는지 저장하는 리스트
    for _ in range(P):
        p = int(input())                            # P번 만큼 정류장의 번호를 입력받는다.
        bus_count.append(counts[p])                 # 해당 정류장의 counts 값을 bus_count에 추가해준다.

    print(f'#{t}', *bus_count)                      # bus_count의 모든 요소 출력(언패킹)
