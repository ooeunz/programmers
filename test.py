# 값 변경 안됨
num = [1, 2, 3]
for i in num:
    i += 1
print(num)
# print => [1, 2, 3]

# 값 변경됨
nums = [[1, 2, 3], [4, 5, 6]]
for i in nums:
    i[0] += 1
print(nums)

# print => [[2, 2, 3], [5, 5, 6]]