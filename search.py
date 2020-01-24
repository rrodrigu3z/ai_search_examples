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

def uniform_cost_search(problem, f):
  node = Node(state=problem.initial_state, path_cost=0)
  frontier = PriorityQueue(f=f)
  frontier.insert(node)
  explored = set()

  while frontier.has_items():
    node = frontier.pop()
    if problem.goal_test(node.state):
      return node.state  # TODO: print solution??
    explored.add(node.state)
    for action in problem.actions(node.state):
      child = node.child_node(problem, action)
      if child.state not in explored and child not in frontier.items():
        frontier.insert(child)
      elif child in frontier.items():
        if f(frontier[child]) > f(child):
          frontier.replace(child, child)

  return None
