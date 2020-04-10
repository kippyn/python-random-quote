import sys

def main(quote):
  print(quote)
  f = open("quotes.txt", "a")
  f.write(quote + "\n")
  f.close()

if __name__== "__main__":
  main(sys.argv[1])