'''prints Star in below format n=5
       *
     * *
   * * *
 * * * * 
* * * * *'''

n = input("enter No : ")

for i in range(int(n)):
    print (" "*(int(n)-i)+"* "*(i+1))