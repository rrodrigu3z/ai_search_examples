class Solution:
  def __init__(self, problem, goal):
    self.goal = goal
    self.problem = problem
    self.action_translations = {
      "up": "arriba",
      "down": "abajo",
      "left": "la izquierda",
      "right": "la derecha"
    }

  def build_humanized_solution(self):
    humanized_solution = []
    for node in reversed(self.goal.path()):
      if node.parent:
        row, col = self.problem.empty_space(node.parent.state)
        tile = node.state[row][col]
        action_translation = self.action_translations[node.action]
        text = "Mover {} hacia {}".format(tile, action_translation)
        humanized_solution.append({"text": text, "node": node})
      else:
        humanized_solution.append({"text": "Estado inicial", "node": node})
    return reversed(humanized_solution)

  def print_solution(self):
    for step in self.build_humanized_solution():
      print(step["text"])
      print("-" * len(step["text"]))
      print(self.pretty_node(step["node"]), "\n")

  def pretty_node(self, node):
    rows = []
    for row in node.state:
      rows.append(" ".join(str(tile) for tile in row))
    return "\n".join(rows)
