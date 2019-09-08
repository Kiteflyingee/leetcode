

def Find( target, array):
    # write code here
    flag = False    #标记是否找到target
    # m,n 分别记录array的行和列
    m, n = len(array), len(array[0])
    if m and n:
      i, j = 0, n
      while i < m and j >= 0:
        #取出矩阵的右上角的值
        right_up = array[i][j-1]
        if right_up == target:
          flag = True
          break
          # 如果右上角值小于目标值，那么去下一行找
        if right_up < target:
          i += 1
        else:
            # 如果右上角值大于于目标值，那么去前一列找
          j -= 1
    return flag


if __name__ == "__main__":
    Find(16 ,[[]])
    pass