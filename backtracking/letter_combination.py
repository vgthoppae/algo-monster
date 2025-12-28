def letter_combination(n: int) -> list[str]:
  result = []

  def dfs(path):
    if len(path) == n:
      result.append("".join(path))
      return

    for letter in "ab":
      path.append(letter)
      dfs(path)
      path.pop()

  dfs([])
  return result

if __name__ == "__main__":
  n = int(input())
  res = letter_combination(n)
  for line in sorted(res):
    print(line)