from collections import deque

def get_neighbors(coord, num_rows, num_cols):
  r, c = coord
  delta_row = [-1, 0, 1, 0]
  delta_col = [0, 1, 0, -1]
  res = []
  for i in range(len(delta_row)):
    neighbor_row = r + delta_row[i]
    neighbor_col = c + delta_col[i]
    if 0<=neighbor_row<num_rows and 0<=neighbor_col<num_cols:
      res.append((neighbor_row, neighbor_col))
  return res

def flood_fill(r: int, c: int, replacement: int, image: list[list[int]]) -> list[list[int]]:
    num_rows = len(image)
    num_cols = len(image[0]) 
    coor_val = image[r][c]
    image[r][c] =  replacement

    root = (r, c)
    q= deque([root])
    visited = set([root])

    while len(q) > 0:
      node = q.popleft()
      r1, c1 = node
      if image[r1][c1] == coor_val:
        image[r1][c1] = replacement
      for neighbor in get_neighbors(node, num_rows, num_cols):
        if neighbor in visited: continue
        nr, nc = neighbor
        if image[nr][nc] == coor_val:
          q.append(neighbor)
        visited.add(neighbor)
      
    return image

if __name__ == "__main__":
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(" ".join(map(str, row)))