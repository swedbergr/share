# Define global variables
MAX_PLAYS = 9
top_left = " "
top_mid = " "
top_right = " "
mid_left = " "
center = " "
mid_right = " "
bottom_left = " "
bottom_mid = " "
bottom_right = " "
tl = False
tm = False
tr = False
ml = False
c = False
mr = False
bl = False
bm = False
br = False

# Sequence of main function
def main():
   # TODO
   pass

# Function that displays the introduction insturctions
def introduction():
  # Display insructions for game
  print("Welcome to Tic Tac Toe!")
  print("The X player will go first. Select the position to play the symbol with",
        "corresponding position.")
  print("TL|TM|TR\n--------\nML| C|MR\n--------\nBL|BM|BR")
  print("Please only use capital letters. Let's get started!")

# Function that displays the board
def display_board():
  # Access global variables
  global top_left, top_mid, top_right, mid_left, center, mid_right,\
  bottom_left, bottom_mid, bottom_right
  # Display baord
  print(f"{top_left}|{top_mid}|{top_right}\n------",
          f"\n{mid_left}|" f"{center}|{mid_right}\n------",
          f"\n{bottom_left}|{bottom_mid}|{bottom_right}")

  

# Function that validates and updates the placement of the board and returns bool
# Returns True if succesful and False if not successful 
def validate_placement(placement, symbol):
  # Access global variables
  global tl, tm, tr, ml, c, mr, bl, bm, br
  global top_left, top_mid, top_right, mid_left, center, mid_right,\
  bottom_left, bottom_mid, bottom_right

  # Check location and assign if available
  if placement == "TL" and not tl:
    top_left = symbol
    tl = True
    return True
  elif placement == "TM" and not tm:
    top_mid = symbol
    tm = True
    return True
  elif placement == "TR" and not tr:
    top_right = symbol
    tr = True
    return True
  elif placement == "ML" and not ml:
    mid_left = symbol
    ml = True
    return True
  elif placement == "C" and not c:
    center = symbol 
    c = True
    return True
  elif placement == "MR" and not mr:
    mid_right = symbol 
    mr = True
    return True
  elif placement == "BL" and not bl:
    bottom_left = symbol
    bl = True
    return True
  elif placement == "BM" and not bm:
    bottom_mid = symbol
    bm = True
    return True
  elif placement == "BR" and not br:
    bottom_right = symbol
    br = True
    return True
  else:
    print("That choice is not an option, please choose a different location.")
    return False

# Function that checks the board to determine if there is a winner
def check_winner(symbol):
  # Access global variables
  global tl, tm, tr, ml, c, mr, bl, bm, br
  global top_left, top_mid, top_right, mid_left, center, mid_right,\
  bottom_left, bottom_mid, bottom_right

  # Check if board has a winning position
  if tl and \
    ((top_left == top_mid and top_left == top_right)\
    or (top_left == center and top_left == bottom_right)\
    or (top_left == mid_left and top_left == bottom_left)):
      print(f"{symbol} wins!!!")
      return True
  if tm and \
    (top_mid == center and top_mid == bottom_mid):
      print(f"{symbol} wins!!!")
      return True
  if tr and \
    (top_right == mid_right and top_right == bottom_right):
      print(f"{symbol} wins!!!")
      return True
  if ml and \
    (mid_left == center and mid_left == mid_right):
      print(f"{symbol} wins!!!")
      return True
  if bl and \
    ((bottom_left == bottom_mid and bottom_left == bottom_right)\
    or (bottom_left == center and bottom_left == top_right)):
      print(f"{symbol} wins!!!")
      return True

  # No winning position
  return False
      


# Execute main function
main()
