def product_of_array_except_self(nums: list[int]) -> list[int]: #[1,2,3,4]
  length = len(nums)
  result = [1] * length

  left = 1
  for i, num in enumerate(nums):
    result[i] = left
    left *= num

  right = 1
  for i in reversed(range(length)):
    result[i] *= right
    right *= nums[i]

  return result

if __name__ == "__main__":
  nums = [int(x) for x in input().split()]
  res = product_of_array_except_self(nums)
  print(" ".join(map(str, res)))