# Create function that simulates a coin
# flip. Each time the function is 
# called, it should randomly select
# either heads or tails and print it 
# out.

import random

def flip():
  output = random.randint(0,1)
  if output == 0:
    print("heads")
  else:
    print("tails")

flip()
