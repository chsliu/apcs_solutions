# F = int(input(""))
# N = int(input(""))
# r = [int(i) for i in input("").split()]

# F = 0
# N = 4
# r = 2, 5, 0, 2
# F = 2
# N = 2
# r = 2, 0
# F = 5
# N = 4
# r = 5, 5, 0, 0
F = 5
N = 6
r = 5, 5, 2, 2, 0, 0

for i in range(0, N):
    if (F == 0 and r[i] == 2) or (F == 2 and r[i] == 5) or (F == 5 and r[i] == 0):
        print(F, end='')
        print(" : "+"Won at round"+str(" ")+str(i+1))
        break
    elif (F == 2 and r[i] == 0) or (F == 5 and r[i] == 2) or (F == 0 and r[i] == 5):
        print(F, end='')
        print(" : "+"Lost at round"+str(" ")+str(i+1))
        break
    else:
        print(F, end=' ')
        if i == N-1:  # 判斷是不是最後一輪
            print(" : "+"Drew at round"+str(" ")+str(i+1))
        if i >= 1:  # 判斷不是第1輪
            # breakpoint()
            if r[i-1] == r[i]:
                if r[i] == 0:
                    F = 5
                elif r[i] == 2:
                    F = 0
                elif r[i] == 5:
                    F = 2
            else:
                # F = r[i-1]
                F = r[i]
