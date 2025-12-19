# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    self.recursively_traverse_inorder(root, result)
    return result

  def recursively_traverse_inorder(self, root: Optional[TreeNode], result: List[int]):
    if not root:
      return
    self.recursively_traverse_inorder(root.left, result)
    result.append(root.val)
    self.recursively_traverse_inorder(root.right, result)

if __name__ == "__main__":
  root = TreeNode(1);
  l1_left = TreeNode(2)
  l1_right = TreeNode(3)
  l2_left2 = TreeNode(5)
  l2_left1 = TreeNode(4)
  l2_right1 = TreeNode(6)
  l2_right2 = TreeNode(7)

  root.left = l1_left
  root.right = l1_right
  l1_left.left = l2_left1
  l1_left.right = l2_left2
  l1_right.left = l2_right1
  l1_right.right = l2_right2

  # root = TreeNode(1);
  # l1_left = TreeNode(2)
  # l1_right = TreeNode(3)
  # l2_left2 = TreeNode(4)
  # l2_right1 = TreeNode(5)
  #
  # root.left = l1_left
  # root.right = l1_right
  # l1_left.right = l2_left2
  # l1_right.left = l2_right1

  result = Solution().inorderTraversal(root)
  print(result)


