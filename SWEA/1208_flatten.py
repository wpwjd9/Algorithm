'''
높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업을 평탄화라고 한다.

가로 길이는 항상 100으로 주어진다.

모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

덤프 횟수는 1이상 1000이하로 주어진다.

주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

'''
# T = int(input())
T = 10
for t in range(1, T + 1):
    dump = int(input())             # 덤프 횟수를 입력받는다.
    arr = list(map(int, input().split()))   # 각 상자의 높이를 입력받는다.
    max_height = 0                  # 최고층을 저장할 변수, 초기값 = 0
    min_height = 10000              # 최저층을 저장할 변수, 초기값 = 10000
    while dump > 0:                 # dump 수 만큼 반복
        max_height_idx = 0          # 최고층의 인덱스를 저장할 변수, 각 덤프마다 0으로 초기화해준다.
        min_height_idx = 0          # 최저층의 인덱스를 저장할 변수
        for i in range(len(arr)):   # 박스열의 개수만큼 반복하는 반복문, arr를 모두 탐색하여 최고층과 최저층을 찾는다.
            if arr[i] >= max_height:
                max_height = arr[i]
                max_height_idx = i
            if min_height >= arr[i]:
                min_height = arr[i]
                min_height_idx = i
        max_height -= 1             # 검사로 찾은 최고층을 한 층 줄여준다.
        arr[max_height_idx] -= 1    # 원본 배열에서 해당하는 인덱스의 값도 1 줄여준다.
        min_height += 1             # 검사로 찾은 최저층을 한 층 높여준다.
        arr[min_height_idx] += 1    # 원본 배열에서 해당하는 인덱스의 값도 1 높여준다.
        dump -= 1                   # dump 횟수 - 1
        for i in range(len(arr)):   # 최고층과 최저층을 마지막으로 검사한다.
            if arr[i] >= max_height:
                max_height = arr[i]
            if min_height >= arr[i]:
                min_height = arr[i]

    print(f'#{t} {max_height - min_height}')  # 최고층과 최저층의 차이를 출력한다.
