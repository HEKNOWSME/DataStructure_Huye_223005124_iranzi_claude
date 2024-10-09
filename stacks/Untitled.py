from collections import deque
bus = deque()
def enqueue(passengers):
   bus.append(passengers)
   print(bus)
def dequeue():
   bus.popleft()
   print(bus)
enqueue('dalia')
enqueue('Genevieve')
dequeue()
