import re

"""

• The ? matches zero or one of the preceding group.
• The * matches zero or more of the preceding group.
• The + matches one or more of the preceding group.
• The {n} matches exactly n of the preceding group.
• The {n,} matches n or more of the preceding group.
• The {,m} matches 0 to m of the preceding group.
• The {n,m} matches at least n and at most m of the preceding group.
• {n,m}? or *? or +? performs a non-greedy match of the preceding group.
• ^spam means the string must begin with spam.
• spam$ means the string must end with spam.
• The . matches any character, except newline characters.
• \d, \w, and \s match a digit, word, or space character, respectively.
• \D, \W, and \S match anything except a digit, word, or space character,
respectively.
• [abc] matches any character between the brackets (such as a, b, or c).
• [^abc] matches any character that isn’t between the brackets.

"""

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

# ^ and $ symbols can be used to search regex that starts and/or ends with with specified pattern

beginsWithHello = re.compile(r'^Hello') # String must start with Hello
print(beginsWithHello.search('Hello is it me you\'re looking for').group())

endsWithHello = re.compile(r'Hello$') # Sting must end with Hello
print(endsWithHello.search('Why, Hello').group())

endsWithDigit = re.compile(r'\d$')
print(endsWithDigit.search('19').group() is not None)

# The Wildcard (.) character

whereTheAtsAt = re.compile(r'.at')
print(whereTheAtsAt.findall('Where the ats at I need that as an expat and that\'s that'))

# Matching everything with dot star

matchEverythingGreedy = re.compile(r'<.*>')
print(matchEverythingGreedy.search('<Match every single> character>').group())

matchEverythingNonGreedy = re.compile(r'<.*?>')
print(matchEverythingNonGreedy.search('<Match every single> character>').group())

# Matching new lines with the dot operator

noNewlineRegex = re.compile(r'.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.'
                       '\nUphold the law.').group())

newlineRegex = re.compile(r'.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.'
                       '\nUphold the law.').group())

# Ignoring casing with re.I

robocop = re.compile('robocop', re.IGNORECASE)
print(robocop.search('ROBOCOP protects the innocent.').group())

# Substituing Strings with the sub() method

secretAgentsRegex = re.compile(r'Agent \w+')
print(secretAgentsRegex.sub('CENSORED', 'Agent Alice gave the documents to Agent Bob.'))

# Managing complex regexes

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
\d{3} # first 3 digits
(\s|-|\.) # separator
\d{4} # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})? # extension
)''', re.VERBOSE)

print(phoneNumberRegex.search('The number is: 555-123-1234') is not None) # True
