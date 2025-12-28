phnum_alpha_map: dict = {
  "2": ["a", "b", "c"],
  "3": ["d", "e", "f"],
  "4": ["g", "h", "i"],
  "5": ["j", "k", "l"],
  "6": ["m", "n", "o"],
  "7": ["p", "q", "r", "s"],
  "8": ["t", "u", "v"],
  "9": ["w", "x", "y", "z"]
}
def letter_combinations_of_phone_number(digits: str) -> list[str]:
  result:list[str] = []

  def get_edges(pos):
    return phnum_alpha_map[digits[pos]]

  def dfs(pos, combo):
    if len(combo) == len(digits):
      result.append("".join(combo))
      return

    for edge in get_edges(pos):
      combo.append(edge)
      dfs(pos+1, combo)
      combo.pop()

  dfs(0, combo=[])
  return result


if __name__ == "__main__":
  digits = input()
  res = letter_combinations_of_phone_number(digits)
  print(" ".join(res))