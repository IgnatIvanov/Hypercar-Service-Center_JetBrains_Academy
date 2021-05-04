from collections import deque

content = deque()
n = int(input())
while n != 0:
    n -= 1
    operation = str(input())
    if 'ENQUEUE' in operation:
        content.append(operation.split()[1])
    elif 'DEQUEUE' in operation:
        content.popleft()

for number in content:
    print(number)
