def generate_parentheses(n: int) -> list[str]:
  res: list[str] = []
  path: list[str] = []

  def dfs(start_index: int, open_count: int, close_count: int) -> None:
    if start_index == 2 * n:
      res.append("".join(path))
      return
    if open_count < n:
      path.append("(")
      dfs(start_index + 1, open_count + 1, close_count)
      path.pop()
    if close_count < open_count:
      path.append(")")
      dfs(start_index + 1, open_count, close_count + 1)
      path.pop()

  dfs(0, 0, 0)
  return res


if __name__ == "__main__":
  n = int(input())
  res = generate_parentheses(n)
  for line in sorted(res):
    print(line)