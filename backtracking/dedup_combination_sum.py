def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
  result = []

  def dfs(start_index, remaining, path):
    if remaining == 0:
      result.append(path)

    for i in range(start_index, len(candidates)):
      num = candidates[i]
      if remaining - num < 0: continue
      dfs(i, remaining-num, path + [num])

  dfs(0, target, [])
  return result


if __name__ == "__main__":
  candidates = [int(x) for x in input().split()]
  target = int(input())
  res = combination_sum(candidates, target)
  for row in sorted(map(sorted, res)):
    print(" ".join(map(str, row)))

# 2 3 6 7