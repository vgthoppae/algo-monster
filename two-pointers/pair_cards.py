def least_consecutive_cards_to_match(cards: list[int]) -> int:
  if len(cards) < 2: return -1 #[3, 4, 2, 3, 4, 7]
  left, right = 0, 1
  window= { #latest position of each card
   cards[0]: 0
  }
  least_cards = 10000000

  while left < right:
    if cards[right] in window:
      left += 1
      least_cards = min(least_cards, right - window[right] + 1)
    window[cards[right]] = right
    if right < len(cards)-1:
      right += 1
    else:
      left += 1
      right = left + 1

  return least_cards


if __name__ == "__main__":
  cards = [int(x) for x in input().split()]
  res = least_consecutive_cards_to_match(cards)
  print(res)