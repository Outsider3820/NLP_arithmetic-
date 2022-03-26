import numpy as np

def edit_distance(sentence1, sentence2):
    len1 = len(sentence1)
    len2 = len(sentence2)
    dp = np.zeros((len1 + 1, len2 + 1))

    for i in range(len1 + 1):
        dp[i][0] = i

    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            temp = 0 if sentence1[i-1] == sentence2[j-1] else 1
            dp[i][j] = min(dp[i-1][j-1] + temp, min(dp[i-1][j] + 1, dp[i][j-1]))
    return dp[len1, len2]

distance = edit_distance("assdds", "sad")
print(distance)
