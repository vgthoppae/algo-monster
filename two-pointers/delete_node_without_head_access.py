class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def delete_node_without_head(head, position):
  curr = head
  cnt = 0

  while curr:
    cnt += 1
    if cnt == position:
      break
    curr = curr.next

  if curr.next:
    curr.val = curr.next.val
    curr.next = curr.next.next

  return head

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
  position = int(input())
  res = delete_node_without_head(head, position)
  print(" ".join(format_list(res)))
