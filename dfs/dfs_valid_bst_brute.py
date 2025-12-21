class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def traverse_in_order(root: Node, vals: list)->list:
  if not root:
    return
  traverse_in_order(root.left, vals)
  vals.append(root.val)
  traverse_in_order(root.right, vals)

def valid_bst(root: Node) -> bool:
  if not root:
    return True
  vals= []
  traverse_in_order(root, vals)
  for i in range(len(vals)-2):
    if vals[i+1] <= vals[i]:
      return False
  return True


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
  res = valid_bst(root)
  print("true" if res else "false")
