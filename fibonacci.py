# def fi(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         result = fi(n - 1) + fi(n - 2)
#     return result
#
# print(fi(5))

# 备忘录
# def fi(n, demo):
#     if n in demo:
#         return demo[n]
#     else:
#         result = fi(n-1, demo) + fi(n-2, demo)
#     demo[n] = result
#     return result
#
# a = {1:1, 2:1}
# print(fi(2, a))

# 动态规划
def fib(n):
    result = {1:1, 2:1}
    if n == 1 or n == 2:
        return 1
    for i in range(3, n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]

print(fib(5))