import re

# The | operator will include either result. It will match the first occurrence:

batRegex = re.compile(r'Batman|Batwoman')
mo = batRegex.search('I\'m Batman, and she\'s Batwoman.')
print(mo.group())  # will return the first occurrence of either Batman or Batwoman

batPrefixRegex = re.compile(r'Bat(man|mobile|copter|cave)')
mo = batPrefixRegex.search('To the Batcave!')
print(mo.group())

# The ? operator will optionally match - meaning it will match either 0 or 1 occurrence:

phoneNumberRegex = re.compile('(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('888-4567')
print(mo.group())

batRegex = re.compile('Bat(wo)?man')
mo = batRegex.search('Batman')  # Will still return a regex match object since 'wo' is optional via ? operator.
print(mo.group())

# The * operator will match zero or more occurrences:

batRegex = re.compile('Bat(wo)*man')
mo = batRegex.search('Batman')
print(mo.group())  # Will still return 'Batman' since matching is optional

# The + operator will match 1 or more occurrences:

batRegex = re.compile('Bat(wo)+man')
mo = batRegex.search('Batman')
print(mo is None)  # Should equate to True since matching in this case was not optional


# The curly braces {} will check for specified number of occurrences

haRegex = re.compile(r'(Ha){3}') # Checks for 3 occurrences 
mo = haRegex.search('HaHaHa')
print(mo.group())

greedyHaRegex = re.compile(r'(Ha){2,5}') # Checks for 2 to 5 occurrences -> will always match longest string
mo = greedyHaRegex.search('HaHaHa')
print(mo.group())

lazyHaRegex = re.compile(r'(Ha){2,5}?') # Lazy regex matching; will match shortest string
mo = lazyHaRegex.search('HaHaHa')
print(mo.group())

# The findall() method will return occurrences found in a list or tuple (if there are groups) format

phoneNumberRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumberRegex.findall('Home: 555-123-4567 Cell: 888-123-6789'))

# Character cases will help you specify what you're looking for

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans,'
                  ' 6 geese, 5 rings, 4 bird3s, 3 hens, 2 doves, 1 partridge'))

# Making your own character classes

vowelRegex = re.compile('[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

vowelRegex = re.compile('[^aeiouAEIOU]') # Adding the ^ operator will exclude these characters
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

vowelRegex = re.compile('[a-z]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

vowelRegex = re.compile('[a-zA-Z0-9]') # Regex object will include all lower and upper case + digits
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# ^ or $ will implement 'starts with' or 'ends with' matching

startsWithRegex = re.compile(r'^Hello')
print(startsWithRegex.search('Hello test me out').group())

startsWithRegex = re.compile(r'Hello$')
print(startsWithRegex.search('Test me out... Hello').group() is None) # False, matches Hello at end