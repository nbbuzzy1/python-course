import re

# search_string = 'search inside of this text'
string = 'search inside of this text please!'
pattern = re.compile('this')
pattern2 = re.compile(r'([a-zA-Z]).([a])')

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.group())
print(b)
print(c)
print(d)

email_pattern = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
