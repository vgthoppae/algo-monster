class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def min_value_node(root):
  curr = root
  while curr and curr.left:
    curr = curr.left
  return curr

def remove(root, val):
  if not root:
    return None

  if val > root.val:
    root.right = remove(root.right, val)
  elif val < root.val:
    root.left = remove(root.left, val)
  else:
    if not root.left:
      return root.right
    elif not root.right:
      return root.left
    else:
      min_node = min_value_node(root.right)
      root.val = min_node.val
      root.right = remove(root.right, root.val)
  return root

if __name__ == "__main__":
  root = TreeNode(4);
  l1_left = TreeNode(3)
  l1_right = TreeNode(6)
  l2_left = TreeNode(2)
  l2_right1 = TreeNode(5)
  l2_right2= TreeNode(7)
  root.left = l1_left
  root.right = l1_right
  l1_left.left = l2_left
  l1_right.left = l2_right1
  l1_right.right = l2_right2
  new_root = remove(root, 3)
  print('done')


