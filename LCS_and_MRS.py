'''
包含leetcode最长公共子序列和最长公共子串

'''
# 寻找最长子序列
def findLength(A, B):
    m, n = len(A) + 1, len(B) + 1
    c = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(m):
        for j in range(n):
    #                 两个数相同
            if i == 0 or j == 0:
                continue
            if A[i-1] == B[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[i][j]


# 最长公共子序列
def findMaximumSeq( A, B) :
    m, n = len(A) + 1, len(B) + 1
    c = [[0 for _ in range(m)] for _ in range(n)]
    
    result = 0  # 用来记录最长的字串长度
    for i in range(1, m):
        for j in range(1, n):
            if A[i-1] == B[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                result = max(result, c[i][j])
    return result

                
if __name__ == "__main__":
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print("maximum len:", findLength(A, B))
    A = [0,0,0,0,0]
    B = [0,0,0,0,0]
    print("maximum len:", findMaximumSeq(A, B))
    pass    