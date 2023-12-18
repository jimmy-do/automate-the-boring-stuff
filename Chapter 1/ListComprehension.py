nums = [1, 2, 3, 4, 5, 6, 7]
evens = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)

evens1 = [n % 2 == 0 for n in nums]
print(evens1)