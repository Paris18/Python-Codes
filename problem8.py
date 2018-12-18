'''Maximum sum of i*arr[i] among all rotations of a given arrayInput : arr[] = {8, 3, 1, 2}
Output : 29
Explanation : Let us see all rotations
{8, 3, 1, 2} = 8*0 + 3*1 + 1*2 + 2*3 = 11
{3, 1, 2, 8} = 3*0 + 1*1 + 2*2 + 8*3 = 29
{1, 2, 8, 3} = 1*0 + 2*1 + 8*2 + 3*3 = 27
{2, 8, 3, 1} = 2*0 + 8*1 + 3*2 + 1*1 = 17

Input : arr[] = {3, 2, 1}
Output : 8'''

import functools
n = input("enter the list: ").split(" ")
n = list(map(int,n))
templist = list(n)
maxx = 0
for i in range(len(n)):
    tempx = (functools.reduce(lambda a,b : a+b,[a*b for a,b in zip(templist,[j for j in range(len(n))])]))
    print (templist,tempx)
    if maxx < tempx:
        maxx = tempx
    templist = templist[-1:]+templist[:-1]
print (maxx)