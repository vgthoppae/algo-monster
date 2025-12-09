from typing import List

class Solution:
  def search(selfs, arr:List, target:int) -> int:
    left = 0
    right = len(arr)-1

    while left <= right:
      mid = (right + left) // 2
      if arr[mid] == target:
        return mid
      elif target > arr[mid]:
        left = mid+1
      elif target < arr[mid]:
        right = mid - 1

    return -1

if __name__ == "__main__":
  s = Solution()
  arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
  print (s.search(arr, 2))