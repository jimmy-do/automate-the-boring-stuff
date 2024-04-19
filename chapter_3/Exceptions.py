def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        return 'Sorry, invalid denominator.'


print(spam(2))
print(spam(0))
