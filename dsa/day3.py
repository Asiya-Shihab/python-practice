arr=[12,35,1,10,34,43,23,42,1]
largest=float('-inf')
secondlargest=float("-inf")
for num in arr:
   if num>largest:
       secondlargest=largest
       largest=num
   elif num>secondlargest and num!=largest:
       secondlargest=num
