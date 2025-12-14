def longest_substring_without_repeating_characters(s: str) -> int:
  left = longest = 0
  window = set()

  for right, c in enumerate(s):
    while c in window:
      window.remove(s[left])
      left += 1
    window.add(c)
    longest = max(longest, len(window))

  return longest


if __name__ == "__main__":
  s = input()
  res = longest_substring_without_repeating_characters(s)
  print(res)