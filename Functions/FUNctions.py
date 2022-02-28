def powerup(x,y,*args):
  result = x
  for i in range(y):
    result = result **2
    print("result is:",result)
  return result

def bday(bdays):
  for b in bdays:
    print(b)
      
bda = [ 1, 19, 1993 ]
bday(bda)