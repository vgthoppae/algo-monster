  # def move_zeros(nums: list[int]) -> None:
  #   # WRITE YOUR BRILLIANT CODE HERE [1, 0, 2, 0, 0, 7]
  #   for slow in range(len(nums)):
  #     if nums[slow] == 0:
  #       fast = slow + 1
  #       while fast <= len(nums) - 1 and nums[fast] == 0:
  #         fast += 1
  #       if fast <= len(nums) - 1:
  #         nums[slow], nums[fast] = nums[fast], nums[slow]
  #
  #   return nums


def move_zeros(nums: list[int]) -> None:
  # WRITE YOUR BRILLIANT CODE HERE [1, 0, 2, 0, 0, 7]
  slow = 0
  for fast in range(len(nums)):
    if nums[fast] != 0:
      nums[slow], nums[fast] = nums[fast], nums[slow]
      slow += 1

  return nums


if __name__ == "__main__":
  nums = [int(x) for x in input().split()]
  move_zeros(nums)
  print(" ".join(map(str, nums)))