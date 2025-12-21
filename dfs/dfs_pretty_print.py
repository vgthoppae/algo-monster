class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

indent_level = ""
def pretty_print(root):
  indent_level = ""
  dfs(root, indent_level)

def dfs(root, indent_level):
  if not root:
    return
  indent_level = indent_level + " "
  print(indent_level + root.val)
  dfs(root.left, indent_level)
  dfs(root.right, indent_level)

if __name__ == "__main__":
  root = TreeNode("/");
  l1_left = TreeNode("Foo")
  l1_right = TreeNode("Bar")
  l2_left = TreeNode("Baz")

  root.left = l1_left
  root.right = l1_right
  l1_left.left = l2_left
  pretty_print(root)