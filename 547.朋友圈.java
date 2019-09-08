/*
 * @lc app=leetcode.cn id=547 lang=java
 *
 * [547] 朋友圈
 */
class Solution {
    public int findCircleNum(int[][] M) {
        // 标记这个同学是否已经被分配了朋友圈
        boolean[] visited = new boolean[M.length];
        int count = 0;
        // 对所有同学整理朋友圈
        for(int i=0; i<M.length; i++){
            if(!visited[i]){
                // 如果这个同学还没有分配进一个朋友圈
                dfs(M, visited, i);
                count++;
            }
        }
        return count;
    }

    // dfs第i个同学的所有朋友
    private void dfs(int[][] m, boolean[] visited, int i) {
        if (visited[i])
            return ;
        visited[i] = true; //标记i被分配好朋友圈
        for(int j=0; j<m.length; j++){
            if(!visited[j] && m[i][j]==1){  //递归找
                dfs(m, visited, j);
            }
        }
    }
}

