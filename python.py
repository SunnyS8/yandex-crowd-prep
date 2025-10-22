nums = [4, 8, 15, 16, 23, 42, 7, 5, 9, 18]

filtered = []
for x in nums:
    if x > 10 and x % 2 == 0:
        filtered.append(x)

print(filtered)
squared = []
for num in filtered:
    squared.append(num ** 2)

print(squared)
