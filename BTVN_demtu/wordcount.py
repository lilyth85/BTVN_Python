
import re
import sys
from collections import Counter


def take_secon(elemm):
    return elemm[1]


# +++your code here+++
def print_words(filename):
  file = open(filename)
  read =file.read().strip().lower()
  cleanString = re.sub("[,.:`?'\-\"\]\[!;)(\*_\n]", '', read)
  li = re.split("\s+", cleanString)
  di = Counter(li).items()
  file.close()
  return di

def print_top(filename):
  file = open(filename)
  read = file.read().strip().lower()
  cleanString = re.sub("[,.:`?'\-\"\]\[!;)(\*_\n]", '', read)
  li = re.split("\s+", cleanString)
  di = Counter(li).items()
  sx = sorted(di, key=take_secon, reverse=True)
  return sx[0:19]

###"alice.txt"

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    for i in  print_top("alice.txt"):
        print(i[0],":",i[1])

    print("===================================================================")
    for i in  print_words("alice.txt"):
        print(i[0],":",i[1])




main()