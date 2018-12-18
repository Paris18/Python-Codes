'''Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''


while True:
   a = input("enter No of a: ")
   if not a:
       break
   n = input("enter value of a: ")
   sumn = 0
   strn = []
   lastsum = 0
   for i in range(a):
       lastsum = lastsum+(10**i)*n
       sumn = sumn+lastsum
       print lastsum
       strn.append('a'*(i+1))
   print strr
   print sumn

   strr = '+'.join(strn)
   print strr
   n = strr.replace('a',str(n))
   print eval(n)