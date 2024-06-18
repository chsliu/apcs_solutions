# N, K = [int(p) for p in input().split()]
# P = [int(p) for p in input().split()]

# N, K = 5, 1
# N, K = 5, 2
N, K = 5, 3
P = [5, 1, 2, 8, 7]

P.sort()

# print(P)
# print("K = ", K)


def canSolve(r):
    start = 0
    k2 = 1
    for i in range(K):
        # print("k", i)
        # print("point", start)
        for s in range(start, N):
            dist = P[s] - P[start]
            if dist > r:
                start = s
                # print("point", start)
                k2 += 1
                break
    # if i > K:
        # return False
    # print("K = ", K)
    # print("r = ", r)
    # print("i", i)
    # print("start", start)
    # return True
    # print("k2 =", k2)
    return k2 <= K


dist = P[-1] - P[0]

minCoverage = 1
maxCoverage = int(dist / K) + 1


# print(canSolve(5))
# print(canSolve(4))
# print(canSolve(3))
# print(canSolve(2))
# print(canSolve(1))

lastmid = 0
while True:
    mid = (minCoverage + maxCoverage) // 2
    # print("mid", mid)

    if mid == lastmid:
        print(maxCoverage)
        break

    if canSolve(mid):
        maxCoverage = mid
        lastmid = mid
    else:
        minCoverage = mid+1
        lastmid = mid
