import pytest
from problem import Problem

p = Problem([(1, 0)], goal=(0, 1))

def test_goal_test():
  assert p.goal_test((1, 2)) == False
  assert p.goal_test((0, 1)) == True

def test_empty_space():
  assert p.empty_space([(1, 2), (0, 3)]) == (1, 0)

def test_actions_all():
  state = [(1, 2, 3), (4, 0, 6), (7, 8, 9)]
  assert p.actions(state) == ["up", "down", "left", "right"]

def test_actions_no_up():
  state = [(1, 2, 3), (4, 1, 6), (7, 0, 9)]
  assert p.actions(state) == ["down", "left", "right"]

def test_actions_no_down():
  state = [(1, 0, 3), (4, 8, 6), (7, 8, 9)]
  assert p.actions(state) == ["up", "left", "right"]

def test_actions_no_left():
  state = [(1, 2, 3), (4, 5, 0), (7, 8, 9)]
  assert p.actions(state) == ["up", "down", "right"]

def test_actions_no_right():
  state = [(1, 2, 3), (0, 5, 6), (7, 8, 9)]
  assert p.actions(state) == ["up", "down", "left"]

def test_actions_only_up_left():
  state = [(0, 2, 3), (4, 5, 6), (7, 8, 9)]
  assert p.actions(state) == ["up", "left"]


def test_actions_only_down_right():
  state = [(1, 2, 3), (4, 5, 6), (7, 8, 0)]
  assert p.actions(state) == ["down", "right"]

def test_up():
  state = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
  expected_state = [[1, 2, 3], [4, 8, 6], [7, 0, 9]]
  assert p.up(state) == expected_state

def test_down():
  state = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
  expected_state = [[1, 0, 3], [4, 2, 6], [7, 8, 9]]
  assert p.down(state) == expected_state

def test_left():
  state = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
  expected_state = [[1, 2, 3], [4, 6, 0], [7, 8, 9]]
  assert p.left(state) == expected_state

def test_right():
  state = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
  expected_state = [[1, 2, 3], [0, 4, 6], [7, 8, 9]]
  assert p.right(state) == expected_state

def test_default_path_cost():
  assert p.path_cost(1) == 2

def test_execute_action():
  state = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
  expected_state = [[1, 2, 3], [4, 8, 6], [7, 0, 9]]
  assert p.execute("up", state) == expected_state

def test_h_misplaced():
  goal = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
  state = [[2, 1, 3], [4, 8, 6], [7, 0, 9]]
  problem = Problem(None, goal=goal)
  assert problem.h_misplaced(state) == 4
