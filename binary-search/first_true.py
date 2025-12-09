from typing import List

class Solution:
  def find_boundary(self, arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
      mid = (left + right) // 2
      if arr[mid] == True:
        first_true_index = mid
        right = mid - 1
      else:
        left = mid + 1

    return first_true_index

if __name__ == "__main__":
  s = Solution()
  arr = [False, False, False, True, True, True, True]
  print (s.find_boundary(arr))