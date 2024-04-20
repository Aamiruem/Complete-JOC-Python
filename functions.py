# def func(L):
#     if L == []:
#         return 0
#     if  L[0] %2 == 0:
#         return 1 + func(L[1:])
#     else:
#         return func(L[1:])









def func(L):
    if L == []:
        return 0
    if  L[-1] %2 == 1:
        return L[-1] + func(L[:-1])
    else:
        return func(L[:-1])

print(func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
