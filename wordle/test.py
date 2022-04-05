#give list of 'a' values and list of 'm' values
def mod(remainder,moduli,multiple):
  if (multiple >= moduli):
    multiple = multiple % moduli
  for i in range(1, 1000):
    if ((i * multiple) % moduli == remainder):
      return i

def lowestMod(multiple, moduli):
  while (multiple > moduli):
    multiple = multiple - moduli
  return multiple
      
  
def Chinese(aList, mList):
  M = 1
  for value in mList:
    M = M * value
  sumTotal = 0
  for i in range(len(aList)):
    aOne = aList[i]
    MOne = M / mList[i]
    yOne = mod(1, mList[i], MOne)
    newProduct = aOne * MOne * yOne
    sumTotal += newProduct
  print(str(sumTotal) + "(mod " + str(M) +")")
  lowestX = lowestMod(sumTotal,M)
  print(lowestX)
   

listOne = [0,8,12]
listTwo = [7,11,13]

Chinese(listOne, listTwo)
