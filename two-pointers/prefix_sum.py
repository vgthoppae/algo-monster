def subarray_sum(arr: list[int], target: int) -> list[int]:
  # WRITE YOUR BRILLIANT CODE HERE  arr = [1, -20, -3, 30, 5, 4], target = 7
  curr_sum = 0
  prefix_sum = {
    0: 0
  }

  for i, num in enumerate(arr):
    curr_sum += num
    if (curr_sum - target) in prefix_sum:
      return [prefix_sum[curr_sum-target], i+1]
    prefix_sum[curr_sum] = i+1

  return []


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  target = int(input())
  res = subarray_sum(arr, target)
  print(" ".join(map(str, res)))