def subarray_sum_shortest(nums: list[int], target: int) -> int: #[1, 4, 1, 7, 3, 0, 2, 5]
  left = smallest = 0
  curr_sum = 0

  for right, num in enumerate(nums):
    curr_sum += num
    while curr_sum >= target:
      smallest = right - left + 1 if smallest == 0 else min(smallest, right - left + 1);
      curr_sum -= nums[left]
      left += 1

  return smallest


if __name__ == "__main__":
  nums = [int(x) for x in input().split()]
  target = int(input())
  res = subarray_sum_shortest(nums, target)
  print(res)