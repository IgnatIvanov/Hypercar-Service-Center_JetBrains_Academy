reversed_queue = deque()
for request in my_queue:
    reversed_queue.appendleft(request)