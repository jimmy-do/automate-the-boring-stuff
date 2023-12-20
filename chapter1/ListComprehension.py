from array import array

nums = [1, 2, 3, 4, 5, 6, 7]
evens = []
odds = []

for n in nums:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)
print(evens)
print(odds)

evens1 = [n for n in nums if n % 2 == 0]
print(evens1)

a = array('i', [3, 2, 1])
a = sorted(a)
print(a)
for i in a:
    print(i)
