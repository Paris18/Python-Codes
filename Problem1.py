'''Problem stmt: Find minimum number of coins/notes needed to calculte a make the change. 
Assume Indian currency denominations [1,2,5,10,20,50,100,200,500,1000,2000].

Example Input : 483
Output: [200, 200, 50, 20, 10, 2, 1]

Example Input : 4989
Output: [2000, 2000, 500, 200, 200, 50, 20, 10, 5, 2, 2]

Example Input : 502
Output: [500, 2]'''

def notesprob(amt):
   currency= [1,2,5,10,20,50,100,200,500,1000,2000]
   reversecurrencylist= reversed(currency)

   lista=[]
   for i in reversecurrencylist:
       if amt >= i:
           j = amt // i
           amt = amt - j * i
           for a in range(0,j):
               lista.append(i)
   print (lista)

#calling function with input
notesprob(1500)"Find minimum number of coins/notes needed to calculte a make the change" 
