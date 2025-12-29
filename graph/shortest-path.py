from collections import deque

def shortest_path(graph: list[list[int]], a: int, b: int) -> int:
  q = deque([a])
  visited = set([a])
  level = -1
  while len(q)>0:
    level += 1
    for _ in range(len(q)):
      node = q.popleft()
      if node == b:
        return level      
      for neighbor in graph[node]:
        if neighbor in visited:
          continue
        q.append(neighbor)
        visited.add(neighbor)

  return 0


if __name__ == "__main__":
  graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
  a = int(input())
  b = int(input())
  res = shortest_path(graph, a, b)
  print(res)