#
# For Else Loop
colors = ['red', 'green', 'blue']
for color in colors:
  if color == 'green':
    print "I wouldn't be seen... in GREEN!"
    break
  print "I'd be caught dead... in", color
else:
  print "AN ANNOUNCEMENT FROM THE GREAT AND POWERFUL OZ"

#
# Is Even Boolean

def is_even(x):
if x % 2 == 0:
  return True
else:
  return False

#
# Is Int

def is_int(x):
  # x = -10.5
  # absolute = 10.5
  # rounded = 11
  # 10.5 - 11 == 0 which is false
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)

#
# Digit Sum 
def digit_sum(n):
  add = []
  total = 0
  for each in str(n):
    total += int(each)
  return total

#
# factorial
def factorial(x):
  #total starts with 1 because anything multiplied by zero equals zero
    total = 1
    #while x is more than zero
    # the total is multiplied by x
    # then the value of x increments down one
    # then returns total once those conditions are not met
    while x>0:
        total *= x
        x-=1
    return total
  
print factorial(5)

#
# Is Prime ***** don't get
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True

print is_prime(13)
print is_prime(10)

#
# Reverse String

def reverse(text):
  arr = []
  for char in text:
    arr.insert(0,char)
  return "".join(arr)

#
# Anti-Vowel
def anti_vowel(text):
    result = ""
    vowels = "ieaouIEAOU"
    for char in text:
          if char not in vowels:
            result += char
    return result
print anti_vowel("hello book")

#
# Scrabble Score
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    total += score[letter]
  return total
