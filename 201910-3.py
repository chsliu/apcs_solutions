class BFSNode:
    # n = 0
    # p = 0
    # l = 0
    # r = 0
    # ls = 0

    def __init__(self, pos, lv):
        self.right = None
        self.left = None
        self.pos = pos
        self.lv = lv

    def config(self, n, p, l, r, board):
        self.n = n
        self.P = p
        self.L = l
        self.R = r
        self.board = board

    def moveLeft(self, n, l, board, pos):
        pos = pos - l
        if pos < 0 or pos > n:
            return -1
        else:
            pos = board[pos]
        return pos

    def moveRight(self, n, r, board, pos):
        pos = pos + r
        if pos < 0 or pos > n:
            return -1
        else:
            pos = board[pos]
        return pos

    def getLeft(self):
        if self.left == None:
            pos = self.moveLeft(self.n, self.L, self.board, self.pos)
            if pos == -1:
                return None
            else:
                self.left = BFSNode(pos, self.lv+1)
                self.left.config(self.n, self.P, self.L, self.R, self.board)
        return self.left

    def getRight(self):
        if self.right == None:
            pos = self.moveRight(self.n, self.R, self.board, self.pos)
            if pos == -1:
                return None
            else:
                self.right = BFSNode(pos, self.lv+1)
                self.right.config(self.n, self.P, self.L, self.R, self.board)
        return self.right

    def goal(self, p):
        q = []
        tNode = self
        lv = 0
        while tNode.pos != p:
            q.append(tNode.getLeft())
            q.append(tNode.getRight())
            # lv = lv + 1
            tNode = q.pop(0)
            while tNode is None:
                if len(q) == 0:
                    print("no steps")
                    return
                tNode = q.pop(0)
            if tNode.pos == p:
                print("steps", tNode.lv)
                return


# def goLeft(n, l, list, pos):
#     pos = pos - l
#     if pos < 0 or pos > n:
#         return -1
#     else:
#         pos = list[pos]
#     return pos


# def goRight(n, r, list, pos):
#     pos = pos + r
#     if pos < 0 or pos > n:
#         return -1
#     else:
#         pos = list[pos]
#     return pos


def main():
    # n,P,L,R = [int(p) for p in input().split()]
    # board = [int(p) for p in input().split()]
    # n, P, L, R = 5, 3, 1, 2
    # board = [0, 2, 4, 3, 1]
    n, P, L, R = 10, 8, 2, 3
    board = [0, 5, 2, 3, 4, 5, 6, 6, 8, 9]

    root = BFSNode(0, 0)
    root.config(n, P, L, R, board)
    root.goal(P)


if __name__ == "__main__":
    main()
