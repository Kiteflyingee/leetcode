/*
 * @lc app=leetcode.cn id=200 lang=java
 *
 * [200] 岛屿数量
 */
class Solution {
    // 记录上下左右4个方向
    int[] px = new int[] { 0, 0, -1, 1 };
    int[] py = new int[] { -1, 1, 0, 0 };

    public int numIslands(char[][] grid) {
        if (grid.length == 0) {
            return 0;
        }
        int count = 0; // 记录岛屿的数量
        // 一个一个遍历所有的点
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    // 遍历他能够访问的所有节点，并把节点清楚掉，表示是一个整体
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length)
            return ;
        if (grid[i][j] == '1') {// 与上一个节点连通，则把这个节点清楚，表示这个节点已经分配好岛屿了
            grid[i][j] = '0';
            for (int x = 0; x < px.length; ++x)
                dfs(grid, i + px[x], j + py[x]);
        }
    }
}
