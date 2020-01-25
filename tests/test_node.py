import pytest
from node import Node
from problem import Problem

def test_equal_nodes():
  node_1 = Node(state=(1, 2))
  node_2 = Node(state=(1, 2), path_cost=3)
  assert node_1 == node_2

def test_less_than_other():
  node_1 = Node(state=(1, 2))
  node_2 = Node(state=(1, 2), path_cost=3)
  assert node_1 < node_2

def test_non_equal_nodes():
  node_1 = Node(state=(0, 0))
  node_2 = Node(state=(1, 2), path_cost=3)
  assert node_1 != node_2

def test_path():
  root_node = Node(state=(1, 2))
  child_1 = Node(state=(3, 4), parent=root_node)
  child_2 = Node(state=(5, 6), parent=child_1)
  assert child_2.path() == [root_node, child_1, child_2]

def test_child_node():
  action = "up"
  problem = Problem([])
  node = Node(state=[[1, 2, 3], [4, 0, 6], [7, 8, 9]])
  child = node.child_node(problem, action)
  assert child.parent == node
  assert child.action == action
  assert child.state == [[1, 2, 3], [4, 8, 6], [7, 0, 9]]
  assert node.state == [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
