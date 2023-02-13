'''
숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.

"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.

입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.

그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.

그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.
'''

def num_count(arr):                         # 각 문자열이 몇 번씩 담겨있는지 세주기 위한 함수
    cnt = [0] * 10
    for num in arr:
        if num == 'ZRO':
            cnt[0] += 1
        elif num == 'ONE':
            cnt[1] += 1
        elif num == 'TWO':
            cnt[2] += 1
        elif num == 'THR':
            cnt[3] += 1
        elif num == 'FOR':
            cnt[4] += 1
        elif num == 'FIV':
            cnt[5] += 1
        elif num == 'SIX':
            cnt[6] += 1
        elif num == 'SVN':
            cnt[7] += 1
        elif num == 'EGT':
            cnt[8] += 1
        else:
            cnt[9] += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    tc, n = map(str, input().split())
    arr = list(map(str, input().split()))
    num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    print(tc)                               # 문자열 그대로 받은 '#테스트 케이스' 출력
    for i in range(10):                     # 0 ~ 9까지
        for _ in range(num_count(arr)[i]):  # cnt 리스트에 담긴 각 요소의 수만큼
            print(num[i], end=' ')          # 문자열과 공백 출력