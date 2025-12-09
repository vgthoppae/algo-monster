from typing import List

class Solution:
  def find_min_rotated(self, arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    boundary_index = -1

    '''
    Intuition:
    Rotated array will have two sorted segments. Move toward the segment that has lower
    value. Using the last element as reference, if the chosen mid is less than that, then
    move to the left, discarding the left
    '''
    while left <= right:
      mid =  left + (right-left)//2
      if arr[mid] <= arr[-1]:
        boundary_index = mid
        right = mid -1
      else:
        left = mid + 1
    return boundary_index

if __name__ == "__main__":
  s = Solution()
  print(s.find_min_rotated([30, 40, 50, 10, 20]))
  print(s.find_min_rotated([3, 5, 7, 11, 13, 17, 19, 2]))
  print(s.find_min_rotated([0,1,2,3,4,5,6]))
  print(s.find_min_rotated([0]))
  print(s.find_min_rotated([5,1,2,3,4]))
  print(s.find_min_rotated([2, 3, 5, 7, 11, 13, 17, 19]))
