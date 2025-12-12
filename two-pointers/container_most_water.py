def container_with_most_water(arr: list[int]) -> int:
  left, right = 0, len(arr)-1
  max_vol = (right - left) * min(arr[left], arr[right])
  while left<right:
    if arr[left] <= arr[right]:
      left += 1
    else:
      right -= 1

    max_vol = max((right-left)*min(arr[left],arr[right]), max_vol)

  return max_vol


if __name__ == "__main__":
  arr = [int(x) for x in input().split()]
  res = container_with_most_water(arr)
  print(res)