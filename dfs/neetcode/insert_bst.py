# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
      return TreeNode(val)

    if val < root.val:
      root.left = self.insertIntoBST(root.left, val)
    elif val > root.val:
      root.right = self.insertIntoBST(root.right, val)

    return root

if __name__ == "__main__":
  # root = TreeNode(5);
  # l1_left = TreeNode(3)
  # l1_right = TreeNode(9)
  # l2_left1 = TreeNode(1)
  # l2_left2 = TreeNode(4)
  #
  # root.left = l1_left
  # root.right = l1_right
  # l1_left.left = l2_left1
  # l1_left.right = l2_left2
  # new_root = Solution().insertIntoBST(root, 6)
  # print('done')
  root = TreeNode(5);
  l1_left = TreeNode(3)
  l1_right = TreeNode(6)
  l2_left = TreeNode(4)
  l2_right = TreeNode(10)
  l3_right = TreeNode(7)

  root.left = l1_left
  root.right = l1_right
  l1_left.right = l2_left
  l1_right.right = l2_right
  l2_right.left = l3_right
  new_root = Solution().insertIntoBST(root, 9)
  print('done')

