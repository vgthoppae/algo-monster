def permutations(letters: str) -> list[str]:
  result = []
  path = []
  used = [False] * len(letters)

  def dfs(start_index):
    if start_index == len(letters):
      result.append("".join(path))
      return

    for i, char in enumerate(letters):
      if used[i]: continue
      path.append(char)
      used[i] = True
      dfs(start_index+1)
      path.pop()
      used[i] = False

  dfs(0)
  return result

if __name__ == "__main__":
  letters = input()
  res = permutations(letters)
  for line in sorted(res):
    print(line)