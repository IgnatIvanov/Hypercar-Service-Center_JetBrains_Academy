from collections import deque

board = deque()
exit_door = deque()

n = int(input())
while n != 0:
    n -= 1
    record = str(input())
    if 'READY' in record:
        board.append(record.split()[1])
    elif 'EXTRA' in record:
        board.append(board.popleft())
    elif 'PASSED' in record:
        # print(board.popleft())
        exit_door.append(board.popleft())

for name in exit_door:
    print(name)
