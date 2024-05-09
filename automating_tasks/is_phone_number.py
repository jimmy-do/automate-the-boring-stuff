# This program checks a string for phone numbers.
import re


def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print(is_phone_number('415-555-4242'))  # Yes, a phone number!
print(is_phone_number('Mochi Ice Cream'))  # Unfortunately, not a phone number!

is_phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = is_phone_regex.search('Check this entire string for a US phone number 415-55-4242')

if mo:
    print('US phone number found: ' + mo.group())
else:
    print('No US phone number found')

