import os
import random

min = os.getenv('MIN_VALUE')
max = os.getenv('MAX_VALUE')


def give_a_num(min_input, max_input):
  try:
    return random.randint(int(min_input), int(max_input))
  except Exception as e:
    print(e)


if __name__ == '__main__':
  print(min, max)
  print(give_a_num(min, max))
