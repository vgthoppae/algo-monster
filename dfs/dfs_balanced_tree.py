class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def is_balanced(tree: Node) -> bool:
  def dfs(root):
    if not root:
      return -1
    left_height = dfs(root.left)
    right_height = dfs(root.right)

    node_height = max(left_height, right_height) + 1

    if abs(left_height - right_height) > 1:
      raise Exception("Not a balanced tree")

    return node_height

  try:
    dfs(tree)
  except Exception:
    return False
  return True

# def is_balanced(tree: Node) -> bool:
#   # Returns (is_balanced, height) where height counts edges
#   def check(node):
#     if node is None:
#       return (True, -1)
#     left_ok, left_h = check(node.left)
#     right_ok, right_h = check(node.right)
#     balanced = left_ok and right_ok and abs(left_h - right_h) <= 1
#     return (balanced, max(left_h, right_h) + 1)
#
#   return check(tree)[0]

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
  tree = build_tree(iter(input().split()), int)
  res = is_balanced(tree)
  print("true" if res else "false")