'''
3
5
1 2 3 4 5
5
4 5 1 2 3
5
5 4 3 2 1
'''

# T = int(input())
# for t in range(1, T + 1):
#     n = int(input())
#     carrots = list(map(int, input().split()))
#     count = 1
#     max_count = 1
#     c_carrot = carrots[0]
#     for i in range(1, len(carrots)):
#         if carrots[i] < c_carrot:
#             count = 1
#             c_carrot = carrots[i]
#         else:
#             count += 1
#             if count >= max_count:
#                 max_count = count
#
#     print(f'#{t} {max_count}')

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    carrots = list(map(int, input().split()))
    count = 1
    max_count = 1
    for i in range(len(carrots) - 1):
        if carrots[i + 1] > carrots[i]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1

    print(f'#{t} {max_count}')