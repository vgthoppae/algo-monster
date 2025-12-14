def subarray_sum_longest(nums: list[int], target: int) -> int:
  left = max_sub = 0
  window_sum = 0

  for right, num in enumerate(nums):
    window_sum += num
    while window_sum > target:
      window_sum -= nums[left]
      left+=1
    max_sub = max(max_sub, right - left + 1)
  return max_sub


if __name__ == "__main__":
  nums = [int(x) for x in input().split()]
  target = int(input())
  res = subarray_sum_longest(nums, target)
  print(res)