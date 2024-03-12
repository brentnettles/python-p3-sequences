#!/usr/bin/env python3

def print_fibonacci(length):
  f = []
  if length == 0:
    print([])
  elif length == 1:
    print([0])
  elif length == 2:
    print([0,1])
  else:
    f = [0,1]

    for count in range(2, length):
      next_count = f[-1] + f[-2]
      f.append(next_count)
    print(f)


# print_fibonacci(10)
