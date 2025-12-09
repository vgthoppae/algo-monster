from typing import List

class Solution:
  def peak_of_mountain_array(self, arr: list[int]) -> int:
    #peak can't at the edges on either side
    left, right = 1, len(arr)-2

    while left<=right:
      mid = left + (right-left)//2

      if arr[mid-1] < arr[mid] > arr[mid+1]:
        return mid
      elif arr[mid] < arr[mid+1]: #going up
        left = mid + 1
      elif arr[mid] > arr[mid+1]: #going down
        right = mid -1

    return -1

if __name__ == "__main__":
  s =Solution()
  # nums = [0, 1, 2, 3, 2, 1, 0]
  # nums = [0,10,3,2,1,0]
  # nums = [0, 10, 0]
  # nums = [0,1,2,12,22,32,42,52,62,72,82,92,102,112,122,132,133,132,111,0]
  # nums = [1,5,4,3,2]
  # nums = [3,9,8,6,4]
  print(s.peak_of_mountain_array(nums))