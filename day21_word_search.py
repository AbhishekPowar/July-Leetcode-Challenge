class Solution:
    def exist(self, board, word):
        def isvalid(i, j):
            return (0 <= i < self.rows) and (0 <= j < self.cols)

        def find(word, idx, i, j, visited):
            if word[idx] == board[i][j]:
                print(word[idx], idx, i, j, visited)
                if self.maxx == idx+1:
                    return True
                if (i, j) not in visited:
                    visited.add((i, j))
                    cmd = ((0, 1), (1, 0), (0, -1), (-1, 0))
                    for dx, dy in cmd:
                        if isvalid(i+dx, j+dy) and (i+dx, j+dy) not in visited:
                            visitedN = visited
                            if find(word, idx+1, i+dx, j+dy, visitedN):
                                return True

                            print('\n')
                    visited.remove((i, j))
                    return False
                else:
                    return False

            else:
                return False

        self.rows = len(board)
        self.cols = len(board[0])
        self.maxx = len(word)
        flag = 0
        for i in range(self.rows):
            for j in range(self.cols):
                print(f'\n_____{i}__{j}____\n')
                ret = find(word, 0, i, j, set())
                if ret:
                    flag = 1
                    break

            if flag:
                break
        return ret


if __name__ == "__main__":
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCEFSADEESE"
    word = "ABCEFSADEESE"
    ans = sol.exist(board, word)
    print(ans)
