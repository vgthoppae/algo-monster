class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def dfs(root):
  return dfs_max(root)

def dfs_max(root):
  if not root:
    return -1
  left_max_val = dfs_max(root.left)
  right_max_val = dfs_max(root.right)
  return max(root.val, left_max_val, right_max_val)

if __name__ == "__main__":
  root = TreeNode(5);
  l1_left = TreeNode(1)
  l1_left1 = TreeNode(8)
  l1_left2 = TreeNode(11)

  root.left = l1_left
  l1_left.left = l1_left1
  l1_left.right = l1_left2

  result = dfs(root)
  print(result)
