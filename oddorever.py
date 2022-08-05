def oddOrEver(num):
 if(num%2) == 0:
  print(f"Число {num} є парним")
 elif (num%2)==1:
  print(f"Число {num} є непарним")

oddOrEver(3)
oddOrEver(8)
oddOrEver(0)
 


x=[0,6,7,8,9]
ever=filter(lambda x: x%2==0,x)
odd=filter(lambda x: x%2==1,x)
print(list(ever),"Числа є парні")
print(list(odd),"Числа є не парні")
