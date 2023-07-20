# from itertools import permutations
# from os import wait4


def weight(n):
    return weights[n-1]


def fetch_count(n):
    return fetchs[n-1]


def get_engergy_from_list(list, n):
    w = 0
    for i in list:
        if i == n:
            return w*fetch_count(i)
        w = w + weight(i)


def total_energy(list):
    te = 0
    for i in list:
        te = te + get_engergy_from_list(list, i)
    return te


def permutations(elements):
    if len(elements) <= 1:
        yield elements
        return
    for perm in permutations(elements[1:]):
        for i in range(len(elements)):
            # nb elements[0:1] works in both string and list contexts
            yield perm[:i] + elements[0:1] + perm[i:]


def all_perms(str):
    if len(str) <= 1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                # nb str[0:1] works in both string and list contexts
                yield perm[:i] + str[0:1] + perm[i:]

# count = int(input())
# weights = [int(p) for p in input().split()]
# fetchs = [int(p) for p in input().split()]

# count = 2
# weights = 20, 10
# fetchs = 1, 1


count = 3
weights = 3, 4, 5
fetchs = 1, 2, 3

# print(count)
# print(weights)
# print(fetchs)

# if count == 2:
#  print("OK")

# list = [1,2]


# print(get_engergy_from_list(list,1))
# print(get_engergy_from_list(list,2))

# print(total_energy(list))


# answers = []
# for i in range(1, count+1):
#     answers.append([i, weight(i)*fetch_count(i)])

# print(answers)
# print(total_energy([2,1]))
# print(total_energy([3,2,1]))

# obj = []
# for i in range(1,count+1):
#  temp = []
#  temp.append(weight(i))
#  temp.append(fetch_count(i))
#  obj.append(temp)
#
# print(obj)

# print(list(permutations([1, 2, 3])))


# print(list(permutations([1, 2, 3])))
ls = []
for i in range(1, count+1):
    ls.append(i)
# print(ls)

lists = list(permutations(ls))
# lists = list(all_perms(ls))
# print(lists)

answers = {}
for l in lists:
    e = total_energy(l)
    answers[e] = l
# print(answers)

answer = list(answers.keys())
answer.sort()
print(answer[0])
