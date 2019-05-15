def printBar(lis): 
  for i in range(len(lis)-1):
    print(lis[i], end='')
  print()

def printTower(tower):
  for i in tower:
    printBar(i)

def makeTower(n):
  first = []
  second = []
  third = []
  for i in range(n, 0, -1):
   first.append(i)
   second.append('-')
   third.append('-')
  first.append('-')
  second.append('-')
  third.append('-')

  return [first, second, third]

def findTop(bar):
  for i in range(len(bar)):
    if bar[i] == '-':
      return i

def check(tower, top):
  From = eval(input("Move from: ")) - 1
  To = eval(input("Move to: ")) - 1 
  retval = [True, From, To]

  barFrom = tower[From][top[From]-1]
  barTo = tower[To][top[To]-1]
  
  if type(barFrom) == type(1) and type(barTo) == type(1):
    if barTo < barFrom:
      print("Cannot put larger on top of smaller. Try again.")
      printTower(tower)
    else:
      retval[0] = not retval[0]
  else:
    retval[0] = not retval[0]
  return retval

def movePiece(tower, n):
  top = []
  for i in tower:
    top.append(findTop(i))

  a = check(tower, top)
  while a[0]:
    a = check(tower, top)

  From = a[1]
  To = a[2]

  temp = tower[From][top[From]-1]
  tower[From][top[From]-1] = tower[To][top[To]]
  tower[To][top[To]] = temp

  printTower(tower)

  if tower[2] == makeTower(n)[0]:
    print("You win!")
    exit(1)

########
# MAIN #
########

if __name__ == '__main__':
  n = eval(input("Please enter the height of the tower: "))
  
  tower = makeTower(n)
  printTower(tower)
  while True:
    movePiece(tower, n)
