def three_sum_unique_triplets(nums: list[int], target: int) -> list[list[int]]:
  result = []
  nums.sort()
  def two_sum(sub_nums: list[int], sub_target: int) -> list[tuple]:
    left, right=0, len(sub_nums)-1

    pairs= []
    while left<right:
      x = sub_nums[left] + sub_nums[right]
      if x == sub_target:
        pairs.append([sub_nums[left], sub_nums[right]])
        while left<right and sub_nums[left] == sub_nums[left+1]:
          left += 1
        while left<right and sub_nums[right] == sub_nums[right-1]:
          right -= 1
        left += 1
        right -= 1
      elif x<sub_target:
        left += 1
      elif x>sub_target:
        right -= 1
    return pairs


  for i, num in enumerate(nums):
    #skip duplicate
    if i>0 and num == nums[i-1]:
      continue

    two_sum_tuples = two_sum(nums[i+1:], target-num)

    for pair in two_sum_tuples:
      result.append([num] + pair)

  return result


if __name__ == "__main__":
  nums = [int(x) for x in input().split()]
  target = int(input())
  res = three_sum_unique_triplets(nums, target)
  for row in res:
    print(" ".join(map(str, row)))