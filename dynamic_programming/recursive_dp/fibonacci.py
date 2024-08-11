def get_fibonacci(n):
  if n == 0: # Base case
    return 0
  if n == 2 or n == 1:  # Base case
    return 1
  prev = 1
  prevprev = 1
  for i in range(3, n+1): # Start from 3
    ans = prev + prevprev # Keep updating prev and prevprev 
    prevprev = prev
    prev = ans
  return ans
