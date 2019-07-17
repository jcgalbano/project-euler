def even_fibonacci_sum_under(limit):
  store = []
  prv = 1
  nxt = 2
  total = 0

  while (prv < limit):
    if (prv%2 == 0):
      total += prv

    tmp = nxt
    nxt = prv + nxt
    prv = tmp

  return total 

print even_fibonacci_sum_under(4000000)
