from typing import List

class Solution:
  def find_first_occurrence(self, arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_occurence_index = -1

    while left <= right:
      mid = (left+right)//2
      if arr[mid] == target:
        first_occurence_index = mid
        right = mid -1
      else:
        left = mid + 1

    return first_occurence_index


if __name__ == "__main__":
  s = Solution()
  arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
  print (s.find_first_occurrence(arr, 3))