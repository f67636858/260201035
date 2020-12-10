a = 2
b = 6
c = -20

root1 = (  ( (-1) * b ) + ( ( ( b**2 ) - (4*a*c) ) ** (1/2) ) )/(2*a)
root2 = (  ( (-1) * b ) - ( ( ( b**2 ) - (4*a*c) ) ** (1/2) ) )/(2*a)

if root1 == root2 :
  print("The root of the equation is "+str(root1))
else:
  print("The roots of the equation are "+ str(root1)+"and"+str(root2))
