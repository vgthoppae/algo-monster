class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def next_node(node):
  return node.next or node

def has_cycle(nodes: Node) -> bool:
  tortoise = next_node(nodes)
  hare = next_node(next_node(nodes))

  while tortoise != hare or not hare.next:
    tortoise = next_node(tortoise)
    hare = next_node(next_node(hare))

  return hare.next is not None


if __name__ == "__main__":
  raw_input = [int(x) for x in input().split()]
  nodes_list = []
  for i in range(len(raw_input)):
    nodes_list.append(Node(i))
  for i, entry in enumerate(raw_input):
    if entry != -1:
      nodes_list[i].next = nodes_list[entry]
  nodes = nodes_list[0]
  res = has_cycle(nodes)
  print("true" if res else "false")