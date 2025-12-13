def subarray_sum_fixed(nums: list[int], k: int) -> int:
  slow = 0
  max_sum = 0
  curr_sum = 0
  for fast in range(len(nums)):
    if fast - slow < k:
      curr_sum += nums[fast]
    else:
      max_sum = max(curr_sum, max_sum)
      curr_sum += nums[fast] - nums[slow]
      slow += 1
  return max(curr_sum, max_sum)


if __name__ == "__main__":
  nums = [int(x) for x in input().split()]
  k = int(input())
  res = subarray_sum_fixed(nums, k)
  print(res)