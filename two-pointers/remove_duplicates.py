def remove_duplicates(arr: list[int]) -> int:
  slow, fast = 0, 0

  for fast in range(len(arr)):
    if arr[fast] != arr[slow]:
      slow += 1
      arr[slow] = arr[fast]

  return slow+1


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  res = remove_duplicates(arr)
  print(" ".join(map(str, arr[:res])))
