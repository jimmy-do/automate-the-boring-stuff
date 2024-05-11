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
print(mo is None)  # should equate to True since matching in this case was not optional

