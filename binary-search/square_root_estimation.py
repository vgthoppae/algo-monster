from typing import List

class Solution:
  def square_root(self, n: int) -> int:
    left, right= 0, n
    candidate = -1

    while left<=right:
      mid = left + (right-left)//2
      n2 = mid * mid
      if n2 == n:
        return mid
      elif n2<n:
        left = mid + 1
        candidate = mid
      elif n2>n:
        right = mid -1

    return candidate

if __name__ == "__main__":
  s = Solution()
  print(s.square_root(2))
  print(s.square_root(3))
  print(s.square_root(5))
  print(s.square_root(6))
  print(s.square_root(7))
  print(s.square_root(11))

  # print(s.square_root(2147395600))
  # print(s.square_root(11))
  # print(s.square_root(4))
  # print(s.square_root(9))
  # print(s.square_root(16))
  # print(s.square_root(25))
  # print(s.square_root(36))
  # print(s.square_root(49))
  # print(s.square_root(64))
  # print(s.square_root(81))
  # print(s.square_root(100))