import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  rnd = random.randint(0, len(quotes)-1)

  # Print and remove newline
  print(quotes[rnd][:-1])

if __name__== "__main__":
  # Print a quote 0-10 times
  for x in range(random.randint(0, 10)):
    primary()