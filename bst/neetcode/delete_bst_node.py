from typing import Optional

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def find_min_node(self, node):
    curr = node
    while curr and curr.left:
      curr = curr.left
    return curr
  def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
      return None

    if key < root.val:
      root.left = self.deleteNode(root.left, key)
    elif key > root.val:
      root.right = self.deleteNode(root.right, key)
    else:
      if not root.left:
        return root.right
      elif not root.right:
        return root.left
      else:
        min_node = self.find_min_node(root.right)
        root.val = min_node.val
        root.right = self.deleteNode(root.right, min_node.val)
    return root

if __name__ == "__main__":
  root = TreeNode(5);
  l1_left = TreeNode(3)
  l1_right = TreeNode(9)
  l2_left1 = TreeNode(1)
  l2_left2 = TreeNode(4)

  root.left = l1_left
  root.right = l1_right
  l1_left.left = l2_left1
  l1_left.right = l2_left2
  new_root = Solution().deleteNode(root, 3)
  print('done')