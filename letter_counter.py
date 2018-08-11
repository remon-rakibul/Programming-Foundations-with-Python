import collections
print('Enter a sentence in which you wanna count letters')
msg = input()
count = {}

for char in msg.upper():
    count.setdefault(char, 0)
    count[char] += 1

for char, nums in dict(collections.OrderedDict(sorted(count.items()))).items():
    print('{} appearred: {} times'.format(char, nums))
