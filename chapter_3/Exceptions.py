def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        return 'Sorry, invalid denominator.'


print(spam(2))
print(spam(0))
