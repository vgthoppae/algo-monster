class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def same_tree(tree1: Node, tree2: Node) -> bool:
  if not tree1 and not tree2:
    return True
  if not tree1 and tree2:
    return False
  if tree1 and not tree2:
    return False

  return (tree1.val == tree2.val and
          same_tree(tree1.left, tree2.left) and
          same_tree(tree1.right, tree2.right))

def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
  if not root or not sub_root:
    return False
  return (same_tree(root, sub_root) or
          same_tree(root.left, sub_root) or
          same_tree(root.right, sub_root))

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
  sub_root = build_tree(iter(input().split()), int)
  res = subtree_of_another_tree(root, sub_root)
  print("true" if res else "false")