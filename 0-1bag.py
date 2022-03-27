import numpy as np

'''
0-1背包
https://www.bilibili.com/video/BV1Cf4y1R7Zz?spm_id_from=333.999.0.0
'''

def bag(info, limit):
    len1 = len(info) + 1
    len2 = limit + 1

    dp = np.zeros((len1, len2))

    for i in range(len1):
        dp[i][0] = 0
    for j in range(len2):
        dp[0][j] = 0

    for i in range(1, len1):
        for j in range(1, len2):
            if info[i-1][1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j-info[i-1][1]] + info[i-1][0], dp[i-1][j])
    return dp[len1-1][len2-1]

items_info = [(6, 3), (10, 1), (5, 2), (10, 4)]
weight_value_dict = {}
limit = 6
print(bag(items_info, limit))
