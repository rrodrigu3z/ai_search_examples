import heapq

class PriorityQueue:
  def __init__(self, f=lambda x: x):
    self.f = f
    self.queue = []

  def insert(self, item):
    weight = self.f(item)
    heapq.heappush(self.queue, (weight, item))

  def items(self):
    return [item[1] for item in self.queue]

  def has_items(self):
    return len(self.queue) > 0

  def pop(self):
    return heapq.heappop(self.queue)

  def replace(self, old_item, new_item):
    index = self.items().index(old_item)
    self.queue[index] = (self.f(new_item), new_item)
    heapq.heapify(self.queue)

  def __getitem__(self, key):
    for _, item in self.queue:
      if item == key:
        return item
