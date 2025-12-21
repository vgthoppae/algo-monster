class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def dfs(root, target):
  if not root:
    return None

  if root.val == target:
    return root

  left = dfs(root.left, target)
  if left: return left
  right = dfs(root.right, target)
  if right: return right


if __name__ == "__main__":
  root = TreeNode(4);
  l1_left = TreeNode(3)
  l1_right = TreeNode(5)
  l2_left = TreeNode(2)
  l2_right = TreeNode(6)

  root.left = l1_left
  root.right = l1_right
  l1_left.left = l2_left
  l1_right.right = l2_right

  result = dfs(root, 6)
  print(result.val)
