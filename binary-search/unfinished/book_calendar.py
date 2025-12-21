class MyCalendar:
  def __init__(self):
    self.calendar = []

  def book(self, start: int, end: int) -> bool:
    left, right, idx = 0, len(self.calendar) - 1, len(self.calendar)
    while left <= right:
      mid = (left + right) // 2
      if self.calendar[mid][0] > start:
        idx = mid
        right = mid - 1
      else:
        left = mid + 1
    # check if calendar[idx-1] or calendar[idx] overlaps with start and end
    if ((idx > 0 and self.calendar[idx - 1][1] > start) or
        (idx < len(self.calendar) and self.calendar[idx][0] < end)):
      return False
    self.calendar.insert(idx, (start, end))
    return True

if __name__ == "__main__":
  c= MyCalendar()
  print(c.book(10, 20));
  print(c.book(20, 30));
  print(c.book(40, 50));
  print(c.book(30, 40));
