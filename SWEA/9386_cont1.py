'''

'''

T = int(input())
for t in range(1, T + 1):
    n = int(input())                    # 숫자의 총 길이
    num_list = list(map(int, input()))  # 입력받은 수를 리스트로 저장
    count = max_count = 0               # 1이 나오면 증가하는 count와 count의 최고값을 저장하기 위한 max_count
    for i in range(n):                  # 수가 나뉘어 저장된 리스트
        if num_list[i] == 0:            # 리스트를 순회하며 0이 나오면 count를 초기화 시켜준다.
            count = 0
        else:                           # 1이 나오면 count를 하나 늘려준다.
            count += 1
            if count > max_count:       # count와 max_count를 비교해 더 큰 값을 max_count에 저장한다.
                max_count = count

    print(f'#{t} {max_count}')