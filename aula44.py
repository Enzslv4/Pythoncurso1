"""
For + range
range -> range(start, stop, step)
start = começo do range
stop = final do range
step = de quanto em quanto pula dentro do range
"""

nums = range(10)
tot = ''
for num in nums:
    tot += f'*{num}'

print(f'{tot}*')