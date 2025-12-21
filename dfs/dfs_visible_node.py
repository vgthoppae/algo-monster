from math import inf

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def visible_tree_node(root: Node) -> int:
  def dfs(root, curr_max:int):
    if not root:
      return 0

    total_visible = 0
    if root.val >= curr_max:
      total_visible += 1

    total_visible += dfs(root.left, max(root.val, curr_max))
    total_visible += dfs(root.right, max(root.val, curr_max))

    return total_visible

  return dfs(root, -inf) if root else 0


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
  val = next(nodes)
  if val == "x":
    return None
  left = build_tree(nodes, f)
  right = build_tree(nodes, f)
  return Node(f(val), left, right)


if __name__ == "__main__":
  root = build_tree(iter(input().split()), int)
  res = visible_tree_node(root)
  print(res)