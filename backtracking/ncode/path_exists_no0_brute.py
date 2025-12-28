class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def path_exists(root: Node, vals:list) -> tuple:
  if not root:
    return True

  if root.val == 0:
    return False
  else:
    vals.append(root.val)

  path = path_exists(root.left, vals)
  if not path:
    path = path_exists(root.right, vals)

  return path


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
  bst = build_tree(iter(input().split()), int)
  vals = []
  res = path_exists(bst, vals)
  print(res)
  print(vals)