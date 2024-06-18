# from memory_profiler import profile


class Node:
    n = 0
    board = []
    lv = 0

    def __init__(self, i, j, lv):
        self.x = i
        self.y = j
        self.level = lv

    def config(self, n, board):
        self.n = n
        self.board = board

    def getXChild(self, cursor, limit):
        childX = cursor.x + 1
        if childX < self.n:
            myH = self.board[cursor.y][cursor.x]
            childH = self.board[cursor.y][childX]
            diffH = myH - childH
            if diffH < 0:
                diffH = -diffH
            if diffH <= limit:
                # print("newchild", childX, cursor.y)
                return Node(childX, cursor.y, cursor.level+1)
        return None

    def getYChild(self, cursor, limit):
        childY = cursor.y + 1
        if childY < self.n:
            myH = self.board[cursor.y][cursor.x]
            childH = self.board[childY][cursor.x]
            diffH = myH - childH
            if diffH < 0:
                diffH = -diffH
            if diffH <= limit:
                # print("newchild", cursor.x, childY)
                return Node(cursor.x, childY, cursor.level+1)
        return None

    def solve(self, limit):
        Q = []
        currentNode = self
        # limit = 4
        # print("Current limit:", limit)

        while currentNode is not None:
            # print("(", currentNode.x, ",", currentNode.y, ")")
            if currentNode.x == self.n-1 and currentNode.y == self.n-1:
                print(limit)
                print(currentNode.level)
                return True

            newChild = self.getXChild(currentNode, limit)
            if newChild is not None:
                Q.append(newChild)

            newChild = self.getYChild(currentNode, limit)
            if newChild is not None:
                Q.append(newChild)

            if len(Q) >= 1:
                currentNode = Q.pop(0)
                # print("currentNode", currentNode.x, currentNode.y)
            else:
                currentNode = None

            # exit()
        return False


# @profile
def main():
    n = int(input(""))
    board = []
    for i in range(n):
        board.append([int(p) for p in input().split()])

    # n = 4
    # board = [[9, 4, 3, 2], [5, 9, 8, 10], [3, 3, 2, 8], [6, 3, 3, 4]]

    # print(n)
    # print(board)

    s = Node(0, 0, 0)
    s.config(n, board)

    limit = 1
    found = s.solve(limit)
    while not found:
        limit += 1
        found = s.solve(limit)


if __name__ == "__main__":
    main()
