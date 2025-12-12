class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def remove_nth_from_end(head, n):
  #dummy is used to handle scenarios when head node is to be removed
  dummy = Node(0, head)
  slow, fast = dummy, dummy
  out_of_bounds = False

  for _ in range(n):
    # if n > size(linked list), catch here and break the loop
    if not fast:
      out_of_bounds = True
      break
    fast = fast.next

  # return the original head as is
  if out_of_bounds:
    return dummy.next

  while fast and fast.next:
    slow = slow.next
    fast = fast.next

  slow.next = slow.next.next

  return dummy.next

# def remove_nth_from_end(head, n):
#   slow, fast = head, head
#   out_of_bounds = False
#   for _ in range(n):
#     if not fast:
#       out_of_bounds = True
#       break
#     fast = fast.next
#
#   if out_of_bounds:
#     return head
#
#   while fast and fast.next:
#     slow = slow.next
#     fast = fast.next
#
#   if fast:
#     slow.next = slow.next.next
#   else:
#     head = slow.next
#   return head

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
  n = int(input())
  res = remove_nth_from_end(head, n)
  print(" ".join(format_list(res)))
