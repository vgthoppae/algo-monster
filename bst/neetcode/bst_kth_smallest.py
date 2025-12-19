# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    result = []
    self.kth_smallest(root, k, result)
    return result.pop() if len(result)>0 else None

  def kth_smallest(self, root: Optional[TreeNode], k: int, result: List[int]):
    if not root:
      return

    self.kth_smallest(root.left, k,result)
    if len(result) == k:
      return
    result.append(root.val)
    self.kth_smallest(root.right, k, result)
    pass


if __name__ == "__main__":
  # root = TreeNode(2);
  # l1_left = TreeNode(1)
  # l1_right = TreeNode(3)
  #
  # root.left = l1_left
  # root.right = l1_right

  root = TreeNode(4);
  l1_left = TreeNode(3)
  l1_right = TreeNode(5)
  l2_left = TreeNode(2)

  root.left = l1_left
  root.right = l1_right
  l1_left.left = l2_left

  result = Solution().kthSmallest(root, 4)
  print(result)
