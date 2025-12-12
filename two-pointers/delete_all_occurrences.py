class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next


def delete_all_occurrences(head, value):
  dummy = Node(0, head)
  slow, fast = dummy, head

  while fast:
    while fast and fast.val == value:
      fast = fast.next

    slow.next = fast
    if fast:
      fast = fast.next
      slow = slow.next

  return dummy.next


def build_list(nodes, f):
  val = next(nodes, None)
  if val is None:
    return None
  nxt = build_list(nodes, f)
  return Node(f(val), nxt)


def format_list(node):
  if node is None:
    return
  yield str(node.val)
  yield from format_list(node.next)

if __name__ == "__main__":
  head = build_list(iter(input().split()), int)
  value = int(input())
  res = delete_all_occurrences(head, value)
  print(" ".join(format_list(res)))