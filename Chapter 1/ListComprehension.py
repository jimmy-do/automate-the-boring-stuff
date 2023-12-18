nums = [1, 2, 3, 4, 5, 6, 7]
evens = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
print(evens)

evenss = [n % 2 == 0 for n in nums]
print(evenss)