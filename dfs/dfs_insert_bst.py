class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def insert_bst(bst: Node, val: int) -> Node:
  if not bst:
    return Node(val)

  if val < bst.val:
    bst.left =  insert_bst(bst.left, val)
  elif val > bst.val:
    bst.right = insert_bst(bst.right, val)
  else: #do nothing - adding just for explicit clarity
    pass

  return bst


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
  val = next(nodes)
  if val == "x":
    return None
  left = build_tree(nodes, f)
  right = build_tree(nodes, f)
  return Node(f(val), left, right)


def format_tree(node):
  if node is None:
    yield "x"
    return
  yield str(node.val)
  yield from format_tree(node.left)
  yield from format_tree(node.right)


if __name__ == "__main__":
  bst = build_tree(iter(input().split()), int)
  val = int(input())
  res = insert_bst(bst, val)
  print(" ".join(format_tree(res)))
