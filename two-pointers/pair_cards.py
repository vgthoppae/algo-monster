def least_consecutive_cards_to_match(cards: list[int]) -> int:
  if len(cards) < 2: return -1 #[3, 4, 2, 3, 4, 7]
  window= { #latest position of each card
   cards[0]: 0
  }
  least_cards = 10000001

  for right in range(1, len(cards)):
    if cards[right] in window:
      least_cards = min(least_cards, right - window[cards[right]] + 1)
    window[cards[right]] = right

  return least_cards if least_cards < 10000001 else -1


if __name__ == "__main__":
  cards = [int(x) for x in input().split()]
  res = least_consecutive_cards_to_match(cards)
  print(res)