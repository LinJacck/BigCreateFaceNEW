from collections import deque

print('from append:\n')
a=['1','2','3','4']
b=deque([])
for e in range(len(a)):
    b.append(a[e])
for i in range(len(b)):
    print(b.popleft())

print('from in')
