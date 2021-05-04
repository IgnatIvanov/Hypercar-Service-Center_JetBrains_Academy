from collections import deque

my_deque = deque()

times = int(input())
while times != 0:
    times -= 1
    command = input()
    if 'ISSUE' in command:
        my_deque.append(command.split()[1])
    elif 'SOLVED' in command:
        my_deque.popleft()

for request in my_deque:
    print(request)
