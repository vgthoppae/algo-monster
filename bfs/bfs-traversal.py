from collections import deque

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def level_order_traversal(root: Node) -> list[list[int]]:
  result = []
  q = deque()
  if root:
    q.append(root)

  while len(q) > 0:
    curr_level_vals = []
    for _ in range(len(q)):
      curr = q.popleft()
      curr_level_vals.append(curr.val)
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
    result.append(curr_level_vals)

  return result


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
  res = level_order_traversal(root)
  for row in res:
    print(" ".join(map(str, row)))