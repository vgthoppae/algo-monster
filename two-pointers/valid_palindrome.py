def is_palindrome(s: str) -> bool:
  left, right = 0, len(s)-1

  while left<right:
    while left<=len(s)-1 and not s[left].isalnum():
      left += 1
    while right>=0 and not s[right].isalnum():
      right -= 1
    if left==len(s) or right==0:
      break
    if s[left].lower() != s[right].lower():
      return False
    left += 1
    right -= 1

  return True


if __name__ == "__main__":
  s = input()
  res = is_palindrome(s)
  print("true" if res else "false")