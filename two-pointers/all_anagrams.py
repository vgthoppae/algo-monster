def find_all_anagrams(original: str, check: str) -> list[int]:
  original_length, check_length = len(original), len(check)
  if original_length < check_length: return []
  check_counter = {}
  def char_counter(word, word_counter):
    for c in word:
      if c in word_counter:
        word_counter[c] += 1
      else:
        word_counter[c] = 1

  char_counter(check, check_counter)
  def is_anagram(window_counter:dict):
    return window_counter == check_counter

  window_counter = {}
  result = []
  for right in range(check_length):
    char_counter(original[right], window_counter)

  if is_anagram(window_counter): result.append(0)

  for right in range(check_length, original_length):
    #remove first char
    c = original[right - check_length]
    if window_counter[c] == 1:
      del window_counter[c]
    else:
      window_counter[c] -= 1
    #add new char
    char_counter(original[right], window_counter)

    if is_anagram(window_counter):
      result.append(right - check_length + 1)

  return result


if __name__ == "__main__":
  original = input()
  check = input()
  res = find_all_anagrams(original, check)
  print(" ".join(map(str, res)))