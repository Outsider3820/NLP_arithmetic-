import numpy as np

'''
硬币找零问题-动态规划
https://www.bilibili.com/video/BV1Ev411q7MC?spm_id_from=333.337.search-card.all.click
'''

def Coin_chage(values, target):
    len1 = len(values) + 1
    len2 = target + 1
    dp = np.zeros((len1, len2))

    for i in range(len1):
        dp[i][0] = 0
    for j in range(len2):
        dp[0][j] = 9999
    for i in range(1, len1):
        for j in range(1, len2):
            if values[i-1] >  j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i][j-values[i-1]] + 1, dp[i-1][j])
    return dp[len1-1][len2-1]

values = [1, 3, 5]
target = 23
print(Coin_chage(values, target))

