def sum_multiples_of_num(mult1, mult2, limit):
    total = 0
    for x in range(1, limit):
      if (x%mult1 == 0) or (x%mult2 == 0):
        total += x
    return total

input_limit = 1000
input_mult1 = 3
input_mult2 = 5

print sum_multiples_of_num(input_mult1, input_mult2, input_limit)
