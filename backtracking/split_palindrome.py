def partition(s: str) -> list[list[str]]:
  result:[list[str]] = []
  def is_palidrome(word):
    return word == word[::-1]

  def dfs(start, cur_path):
    if start == len(s):
      result.append(cur_path[::])
      return

    for end in range(start+1, len(s)+1):
      prefix= s[start:end]
      if is_palidrome(prefix):
        dfs(end, cur_path+[prefix])

  dfs(0, [])
  return result


if __name__ == "__main__":
  s = input()
  res = partition(s)
  for row in res:
    print(" ".join(row))