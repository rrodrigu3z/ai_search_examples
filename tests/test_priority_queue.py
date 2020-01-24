import pytest
from priority_queue import PriorityQueue

def test_empty_queue():
  pq = PriorityQueue()
  assert pq.items() == []

def test_insert_item():
  pq = PriorityQueue()
  pq.insert(1)
  assert pq.queue == [(1, 1)]
  assert pq.items() == [1]

def test_get_item():
  pq = PriorityQueue()
  pq.insert(1)
  assert pq[1] == 1

def test_custom_function():
  pq = PriorityQueue(f=lambda x: (x * 2))
  pq.insert(1)
  pq.insert(2)
  assert pq.queue == [(2, 1), (4, 2)]

def test_replace_item():
  pq = PriorityQueue()
  pq.insert(1)
  pq.insert(5)
  pq.replace(5, 3)
  assert pq.queue == [(1, 1), (3, 3)]

def test_has_items():
  pq = PriorityQueue()
  assert pq.has_items() == False
  pq.insert(1)
  assert pq.has_items() == True

def test_pop_by_min_priority():
  pq = PriorityQueue()
  pq.insert(2)
  pq.insert(1)
  pq.insert(3)
  assert pq.pop() == (1, 1)
  assert pq.queue == [(2,2), (3,3)]
