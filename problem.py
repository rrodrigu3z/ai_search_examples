
class Problem:
  def __init__(self, initial_state, goal=None, f_cost=lambda x: x+1):
    self.initial_state = initial_state
    self.goal = goal
    self.f_cost = f_cost
    self.rules = {
      "up":    {"rows": (0, 1),    "cols": (0, 1, 2)},
      "down":  {"rows": (1, 2),    "cols": (0, 1, 2)},
      "left":  {"rows": (0, 1, 2), "cols": (0, 1)},
      "right": {"rows": (0, 1, 2), "cols": (1, 2)}
    }

  def goal_test(self, state):
    return state == self.goal

  def path_cost(self, previous_cost):
    return self.f_cost(previous_cost)

  def execute(self, action, state):
    action_method = getattr(self, action)
    return action_method(list(state))

  def actions(self, state):
    empty_coords = self.empty_space(state)
    # lambda para filtrar movimientos válidos
    def rule_processor(action):
      return empty_coords[0] in self.rules[action]["rows"] and \
             empty_coords[1] in self.rules[action]["cols"]

    return list(filter(rule_processor, self.rules))

  def empty_space(self, state):
    for row, cols in enumerate(state):
      for col, value in enumerate(cols):
        if value == 0:
          return row, col

  def swap(self, state, row, col, new_rol, new_col):
    state[new_rol][new_col] = state[row][col]
    state[row][col] = 0
    return state

  def up(self, state):
    row, col = self.empty_space(state)
    return self.swap(state, row + 1, col, row, col)

  def down(self, state):
    row, col = self.empty_space(state)
    return self.swap(state, row - 1, col, row, col)

  def left(self, state):
    row, col = self.empty_space(state)
    return self.swap(state, row, col + 1, row, col)

  def right(self, state):
    row, col = self.empty_space(state)
    return self.swap(state, row, col - 1, row, col)

  def h_misplaced(self, state):
    count = 0
    for i in range(0, len(self.goal)):
      for j in range(0, len(self.goal[0])):
        if self.goal[i][j] != state[i][j]:
          count += 1
    return count
