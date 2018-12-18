'''Challenge 11:
Search an element in a sorted and circular array

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
        key = 3
Output : Found at index 8

Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
        key = 30
Output : Not found

Input : arr[] = {30, 40, 50, 10, 20}
       key = 10  
Output : Found at index 3'''

lista = [5,6,7,8,9,1,2,3,4]
key = int(input("enter key to search: "))

def binarysearch(l,r):
    global index
    if l <= r:
        mid = (l+r)//2
        if key == lista[mid]:
            return mid
        elif (lista[l] <= lista[mid-1]):
            if key in lista[l:mid]:
                return binarysearch(l,mid-1)
            else:
                return binarysearch(mid+1,r)
        else:
            if key in lista[mid:r]:
                return binarysearch(mid+1,r)
            else:
                return binarysearch(l,mid-1)
    return None
        
index = binarysearch(0,len(lista))
if index != None:
    print (index)
else:
    print ("Key not exists")