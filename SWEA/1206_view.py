'''
왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보된다고 말한다.
빌딩들에 대한 정보가 주어질 때, 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성하시오.

총 10개의 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에느느 건물의 개수 n이 주어진다.
그 다음 줄에는 n개의 건물의 높이가 주어진다.
맨 왼쪽 두 칸과 맨 오른쪽 두 칸에 있는 건물은 항상 높이가 0이다.
#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 조망권이 확보된 세대의 수를 출력한다.
'''


T = int(input())    # 테스트 케이스의 수를 입력받는다.
for t in range(1, T + 1):   # 테스트 케이스의 수만큼 반복하는 반복문
    n = int(input())    # 건물의 개수를 입력받는다.
    b_height = list(map(int, input().split()))  # 각 건물의 높이를 입력받는다. split하여 list형태로 저장한다.
    total = 0   # 조망권이 확보된 총 세대의 수를 저장하기 위한 total
    for i in range(2, n - 2):   # 맨 왼쪽 두칸과 맨 오른쪽 두 칸은 0으로 되어있기 때문에 그것을 제외한 범위에 대한 반복문
        # 해당 건물을 기준으로 왼쪽 두 칸 내에 더 높은 건물이 있을 경우, 왼쪽으로 뷰가 있는 세대의 수를 저장하는 l_view를 0으로 저장한다.
        if b_height[i - 1] > b_height[i] or b_height[i - 2] > b_height[i]:
            l_view = 0
        # 해당 건물을 기준으로 오른쪽 두 칸 내에 더 높은 건물이 있을 경우, 왼쪽으로 뷰가 있는 세대의 수를 저장하는 r_view를 0으로 저장한다.
        elif b_height[i + 1] > b_height[i] or b_height[i + 2] > b_height[i]:
            r_view = 0
        # 둘 다 아닐 경우
        else:
            # 바로 옆 건물이 두 칸 옆 건물보다 높을 경우(왼쪽)
            if b_height[i - 1] > b_height[i - 2]:
                l_view = b_height[i] - b_height[i - 1]
            else:
                l_view = b_height[i] - b_height[i - 2]
            # 바로 옆 건물이 두 칸 옆 건물보다 높을 경우(오른쪽)
            if b_height[i + 1] > b_height[i + 2]:
                r_view = b_height[i] - b_height[i + 1]
            else:
                r_view = b_height[i] - b_height[i + 2]
        # 위와 같은 조건문을 통해 구해진 l_view와 r_view 중 더 낮은 값만을 t_view에 저장한다.
        if l_view > r_view:
            t_view = r_view
        else:
            t_view = l_view
        # 모든 건물에 대한 t_view를 합하여 total에 저장한다.
        total += t_view
    print(f'#{t} {total}')