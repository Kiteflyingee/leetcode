#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (38.88%)
# Likes:    202
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 48.1K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true.
# 给定 word = "SEE", 返回 true.
# 给定 word = "ABCB", 返回 false.
#
#


class Solution:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.py = [-1, 1, 0, 0]
        self.px = [0, 0, -1, 1]

    def exist(self, board, word):
        visited = set()  # 记录路径上访问过的节点
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, visited):
                    return True
        return False

    def dfs(self, board, word, i, j, visited):
        # dfs这个节点的所有可能的值
        if word == "":
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        # 把当前节点添加到以访问
        visited.add((i, j))
        result = False
        for pi in range(len(self.px)):
            x = i + self.px[pi]
            y = j + self.py[pi]
            if (x, y) not in visited:
                result = result or self.dfs(board, word[1:], x, y, visited)
        # 这个节点路径全部访问过了，去出这个节点
        visited.remove((i, j))
        return result


if __name__ == "__main__":
    print(Solution().exist(
        [["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "E"]], "ABCESEEEFS"))
