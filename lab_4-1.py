# Author: EBP (AMDG) 11/16/20

colors = ['red', 'blue', 'yellow']
print(colors)

colors.extend(['purple', 'green', 'gold'])
print(colors)

print(colors.count('yellow'))

colors.insert(3, 'navy')
print(colors)

colors.clear()
print(colors)

print(colors.count('red'))