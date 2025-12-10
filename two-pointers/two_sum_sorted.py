def two_sum_sorted(arr: list[int], target: int) -> list[int]:
  left, right = 0, len(arr)-1

  while left<right:
    if arr[left] + arr[right] == target:
      return [left, right]
    elif arr[left] + arr[right] < target:
      left += 1
    else:
      right -= 1

  return None


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  target = int(input())
  res = two_sum_sorted(arr, target)
  print(" ".join(map(str, res)))
