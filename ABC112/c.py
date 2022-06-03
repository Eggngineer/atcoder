import sys
input = sys.stdin.readline

N = int(input().rstrip('\n'))

# P(x,y,h)
P = [list(map(int, input().rstrip('\n').split())) for _ in range(N)]

for (x,y,h) in P:
    if h == 0:
        continue
    else:
        asm = [x,y,h]
        break

_x,_y,_h = 0,1,2
for cx in range(100+1):
    for cy in range(100+1):
        manhattan = abs(cx-asm[_x]) + abs(cy-asm[_y])
        pred_H = asm[_h]+manhattan

        for (x,y,h) in P:
            if max(pred_H - abs(cx-x) - abs(cy-y), 0) != h:
                break
        else:
            print(cx,cy,pred_H)

# # print(pred_H)

# N = int(input())  # 標準入力
# P = []
# for i in range(N):
#     x, y, h = map(int, input().split())
#     P.append([h, x, y])
# P.sort(reverse=True)  # hの降順で観測値をソート
 
 
# def calc_H(c_x, c_y, x, y, h) -> int:
#     return h + abs(c_x - x) + abs(c_y - y)
 
 
# # Hは上限がない=>C_xとC_yで全探索していけばいい！
# for C_x in range(0, 101):
#     for C_y in range(0, 101):
#         for i in range(N):
#             X, Y, h_actual = P[i][1], P[i][2], P[i][0]
#             if i == 0:
#                 H_ori = calc_H(C_x, C_y, X, Y, h_actual)
#             elif max(H_ori - abs(C_x - X) - abs(C_y - Y), 0) != h_actual:
#                 break
#         else:  # breakされずに最後までいけば...
#             print(f"{C_x} {C_y} {H_ori}")