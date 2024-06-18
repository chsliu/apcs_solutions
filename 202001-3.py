# N,L = [int(i) for i in input().split()]
# pos = [int(i) for i in input().split()]
# hei = [int(i) for i in input().split()]
N, L = 6, 140
pos = [10, 30, 50, 70, 100, 125]
hei = [30, 15, 55, 10, 55, 25]

# answer1 = 0
# answer2 = []
# check = True

# pos.append(L)
# hei.append(0)
# pos.insert(0,0)
# hei.insert(0,0)
# print(pos)
# print(hei)

# while check:
#   if len(pos) >= 3:
#     for i in range(1,len(pos)):
#       if pos[i]-hei[i] >= pos[i-1] and pos[i]+hei[i] <= pos[i+1]:
#         answer1 += 1
#         answer2.append(hei[i])
#         pos.pop(i)
#         hei.pop(i)
#         break
#       else:
#         check = False
#   else:
#     check = False

# print(answer1,answer2)

lastcnt = 0
cnt = 0
maxH = 0
i = 0

while True:
    chop = False
    if i == 0 and pos[i] - hei[i] >= 0:
        chop = True
    elif i >= 1 and pos[i] - hei[i] >= pos[i-1]:
        chop = True
    elif i == len(pos)-1 and pos[i] + hei[i] <= L:
        chop = True
    elif i < len(pos)-1 and pos[i] + hei[i] <= pos[i+1]:
        chop = True

    if chop:
        cnt += 1
        if hei[i] > maxH:
            maxH = hei[i]
        pos.pop(i)
        hei.pop(i)

    i += 1
    if i >= len(pos):
        i = 0

        if lastcnt == cnt:
            break

        lastcnt = cnt

# print(pos)
# print(hei)
print(cnt)
print(maxH)
