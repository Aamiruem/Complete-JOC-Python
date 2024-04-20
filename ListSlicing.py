# L = [90, 47, 8, 18, 10, 7]
# s = [L[0]]

# for i in range(1, len(L)):
#     flag = True
#     for j in range(len(s)):
#         if L[i] > s[j]:
#             before_j = s[:j]
#             new_j = [L[i]]  # Wrap L[i] in a list to append it as a single element
#             after_j = s[j:]
#             s = before_j + new_j + after_j
#             flag = False
#             break
#     if flag:
#         s.append(L[i])

# print(s)
# Output: [90, 47, 8, 18, 10, 7]







L = [90, 47, 8, 18, 10, 7]
s = [L[0]]

for i in range(1, len(L)):
    flag = True
    for j in range(len(s)):
        if L[i] < s[j]:
            before_j = s[:j]
            new_j = [L[i]]  # Wrap L[i] in a list to append it as a single element
            after_j = s[j:]
            s = before_j + new_j + after_j
            flag = False
            break
    if flag:
        s.append(L[i])
print(s)
