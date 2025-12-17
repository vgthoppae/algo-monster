def range_sum_query_immutable(nums: list[int], left: int, right: int) -> int:
  # WRITE YOUR BRILLIANT CODE HERE Input: nums = [1, 2, 3, 4], sumRange(1, 3). Output: 9.
  prefix_sum = {0:0}
  curr_sum = 0

  for i, num in enumerate(nums):
    curr_sum += num
    prefix_sum[i+1] = curr_sum

  return prefix_sum[right+1]-prefix_sum[left]


if __name__ == "__main__":
  nums = [int(x) for x in input().split()]
  left = int(input())
  right = int(input())
  res = range_sum_query_immutable(nums, left, right)
  print(res)