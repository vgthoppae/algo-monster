from collections import Counter
def subarray_sum_total(arr: list[int], target: int) -> int:
  # WRITE YOUR BRILLIANT CODE HERE  arr = [1, -20, -3, 30, 5, 4], target = 7
  curr_sum = 0
  prefix_sum: Counter[int] = Counter()
  prefix_sum[0] = 1
  count = 0
  for i, num in enumerate(arr):
    curr_sum += num
    complement = curr_sum - target
    if complement in prefix_sum:
      count += prefix_sum[complement]
    prefix_sum[curr_sum] += 1
  return count


if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_total(arr, target)
    print(res)