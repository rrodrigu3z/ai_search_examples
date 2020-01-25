import copy

class Node:
  def __init__(self, state=None, parent=None, path_cost=1, action=None):
    self.state = state
    self.path_cost = path_cost
    self.parent = parent
    self.action = action

  def child_node(self, problem, action):
    new_state = problem.execute(action, copy.deepcopy(self.state))
    new_state_cost = problem.path_cost(self.path_cost)
    return Node(state=new_state,
                parent=self,
                path_cost=new_state_cost,
                action=action)

  def path(self, full_path=[]):
    node = self
    full_path = []
    # Recorrer todos los padres hasta la raíz
    while node:
      full_path.insert(0, node)
      node = node.parent

    return full_path

  def __eq__(self, other):
    return other.state == self.state

  def __lt__(self, other):
    return self.path_cost < other.path_cost
