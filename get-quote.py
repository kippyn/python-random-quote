import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  rnd = random.randint(0, len(quotes)-1)
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  primary()
