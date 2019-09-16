def fibIterative(n: int) -> int:
  if n == 0: return n
  last: int = 0
  next: int = 1

  for _ in range(1, n):
    tmp = next
    next = last + next
    last = tmp

    # A more concise way to do the above:
    #last, next = next, last + next
  
  return next

if __name__ == "__main__":
  print(fibIterative(-10))
