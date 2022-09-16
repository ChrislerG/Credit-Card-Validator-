def getSize(d):
  d = str(d)  
  
  return (len(d)) 
  
def getPrefix(number, k):
  save_list = []
  if k > len(number):
    return number
  else:
    for i in range(len(number)):
      if i < k:
        save_list.append(number)
        saved =''.join(save_list)
        return saved 
      

  
def prefixMatched(number,d):
  save_list = []
  for i in range(len(d)):
      if i == '4':
        
        save_list.append(number)
        print('this is a visa card') 
      elif i == '5':
        save_list.append(number)
        print('this is a Mastercard card')
      elif i == '3':
        save_list.append(number)
        print('this is a American Express card')
      elif i == '6':
        save_list.append(number)
        print('this is a Discover card')
      else:
        print('This card number is invalid')
      saved ='' .join(save_list)
      return True
def getDigit(number): 

  if len(number) == 1:
    return number 
  else: 
    sum = number[0] + number[1] 
    return sum 
  print(getDigit(''))

def sumOfDoubleEvenPlace(number):  
  save_even_list = [] 
  
  #number = int(number)
  for i in range(len(number)):
   i % 2 == 0
  num = number[i] * 2 
  num = str(num) 
  number = getDigit(num) 

  number = str(number)
  
  save_even_list.append(number)
  

  for i in range(len(save_even_list)):
    
    sum = int(save_even_list[0])
    sum = sum + int(save_even_list[i])
  sum = str(sum)
  
  return sum 
  
 
  

def sumofOddPlace(number):
  save_odd_list = []
  index = 0
  while index < (len(number)): 
    if index % 2 != 0:
     save_odd_list.append(number[index])
    index = index + 1
  total = 0
  for index in range(len(save_odd_list)):
      total = total + int(save_odd_list[index]) 
  return total




def isValid(number):
  if getSize(number) > 12 and getSize(number) < 17:  
    prefix1 = getPrefix(number, 1)
    prefix2 = getPrefix(number, 2) 
    matched1 = prefixMatched(number, prefix1) 
    matched2 = prefixMatched(number, prefix2)
   
    if matched1 == True or matched2 == True:

      sum1 = sumOfDoubleEvenPlace(number)
      sum2 = sumofOddPlace(number) 

      total = sum1 + sum2  

      if total % 10 == 0: 
        return True
      else:
        return False
    else:
      return False
  else: 
    return False 