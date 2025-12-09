from typing import List

class Solution:
  def first_not_smaller(self, arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_not_smaller_index = -1

    while left <= right:
      mid = (left+right)//2
      if arr[mid] >= target:
        first_not_smaller_index = mid
        right = mid -1
      else:
        left = mid + 1

    return first_not_smaller_index


if __name__ == "__main__":
  s = Solution()
  arr = [1, 3, 3, 5, 8, 8, 10]
  print (s.first_not_smaller(arr, 2))