# class Solution:
#     def findCircleNum(self, M):

#         queue, cnt = [0], 0  # [0] 表示第一个人，题目已经给出至少一个人。 cnt 记录朋友圈的个数
#         visited = [0] * len(M)  # 0 表示没有访问过，1 表示已经访问过了。
#         visited[0] = 1

#         while len(queue):  # 队列不为空
#             i = queue.pop()  # 出队一个人
#             for j in range(len(M[i])):
#                 if visited[j] or i == j or M[i][j] == 0:  # 访问过了，或者是自己，或者不是朋友关系，则不加
#                     continue
#                 if M[i][j]>3:
#                     queue.append(j)  # 入队
#                 visited[j] = 1  # 此人已经访问过

#             if not len(queue):  # 队列为空
#                 cnt += 1  # 朋友圈数 加一
#                 if sum(visited) < len(visited):  # 如何还有人没有被分到朋友圈
#                     idx = visited.index(0)  # 继续入队一个人
#                     queue.append(idx)
#                     visited[idx] = 1
#         return cnt


class Solution:
    def findCircleNum(self, M) :
        n = len(M)
        p = {i: {i} for i in range(n)}  #并查集初始化
        ans = n
        for i in range(n):
            for j in range(i, n):       #遍历邻接矩阵
                if M[i][j] > 3 and p[i] is not p[j]:
                    p[i] |= p[j]        #集合合并
                    for k in p[j]:      #改变被合并的集合内元素指向
                        p[k] = p[i]
                    ans -= 1            #减少朋友圈
        return ans


if __name__ == '__main__':
    N = int(input())
    rows = []
    for _ in range(N):
        row = list(map(int, input().split()))
        rows.append(row)
    solu = Solution()
    print(solu.findCircleNum(rows))