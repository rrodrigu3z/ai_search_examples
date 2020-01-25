# function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
#   node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
#   frontier ← a priority queue ordered by PATH-COST, with node as the only element
#   explored ←an empty set
#   loop do
#     if EMPTY?(frontier ) then return failure
#     node ← POP(frontier ) /* chooses the lowest-cost node in frontier */
#     if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
#     add node.STATE to explored
#     for each action in problem.ACTIONS(node.STATE) do
#       child ← CHILD-NODE(problem, node, action)
#       if child.STATE is not in explored or frontier then
#         frontier ← INSERT(child,frontier )
#       else if child.STATE is in frontier with higher PATH-COST then
#         replace that frontier node with child

from priority_queue import PriorityQueue
from node import Node
from problem import Problem

def uniform_cost_search(problem, f):
  node = Node(state=problem.initial_state, path_cost=0)
  frontier = PriorityQueue(f=f)
  frontier.insert(node)
  explored = []

  while frontier.has_items():
    _, node = frontier.pop()
    if problem.goal_test(node.state):
      return node  # TODO: print solution??
    explored.append(node.state)
    for action in problem.actions(node.state):
      child = node.child_node(problem, action)
      if child.state not in explored and child not in frontier.items():
        frontier.insert(child)
      elif child in frontier.items():
        if f(frontier[child]) > f(child):
          frontier.replace(child, child)

  return None


def astar_search(problem, h=None):
    """A* es una implementación de búsqueda best-first pero usando
    heurística, donde f(n) = g(n) + h(n). A su vez, best-first es
    igual a uniform-cost pero usando f(n) para ordenar los elementos
    en la cola de prioridades"""
    return uniform_cost_search(problem, f=lambda n: n.path_cost + h(n))

def h_misplaced(node):
  return problem.h_misplaced(node.state)

initial = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
problem = Problem(initial, goal=goal)

solution = astar_search(problem, h=h_misplaced)
print(solution.state)
print(list(map(lambda n: n.state, solution.path())))
