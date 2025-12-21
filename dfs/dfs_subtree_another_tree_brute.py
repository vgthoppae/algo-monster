class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def traverse_tree(root: Node) -> tuple:
  if not root:
    return (-1, [])

  (left_depth, left_tree_vals) = traverse_tree(root.left)
  (right_depth, right_tree_vals) = traverse_tree(root.right)
  tree_vals = left_tree_vals
  tree_vals.append(root.val)
  tree_vals += right_tree_vals
  node_depth = max(left_depth, right_depth) + 1

  return (node_depth, tree_vals)

def does_match(root, sub_tree_depth, sub_tree_vals) -> bool:
  (parent_tree_depth, parent_tree_vals) = traverse_tree(root)
  return (parent_tree_depth == sub_tree_depth and
          parent_tree_vals == sub_tree_vals)

def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
  # traverse the subtree - height of the tree and node values with inorder traversals
  (sub_tree_depth, sub_tree_vals) = traverse_tree(sub_root)
  #traverse the main tree and look for a match on the subtree root val
  if not root:
    return False
  right_node = root.right
  while root:
    if root.val == sub_root.val:
      match = does_match(root, sub_tree_depth, sub_tree_vals)
      if match: return True
    root = root.left

  root = right_node
  while root:
    if root.val == sub_root.val:
      match = does_match(root, sub_tree_depth, sub_tree_vals)
      if match: return True
    root = root.right

  return False

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