

class Node():
	def __init__(self,data):
		self.data = data
		self.next=None


class Lnlist():
	def __init__(self):
		self.head = None


def push(data,llist):
	newnode = Node(data)
	newnode.next = llist.head
	llist.head = newnode
	return llist


def append(data,llist):
	ldata = llist.head
	while (ldata.next !=None):
		ldata = ldata.next
	ldata.next = Node(data)
	return llist

def insert(data,llist,index):
	Lenght = 0
	ldata = llist.head
	newnode = Node(data)
	if(index == 0):
		newnode.next = llist.head
		llist.head = newnode
	else:
		while (ldata.next !=None):
			if (index == Lenght):
				break
			else:
				ldata = ldata.next
				Lenght += 1
		newnode.next = ldata.next
		ldata.next = newnode
	return llist

def pop(llist,index):
	Lenght = 0
	ldata = llist.head
	if(index == 0):
		llist.head = llist.head.next

	else:
		while (ldata !=None):
			if (index-1 == Lenght):
				if(ldata.next.next == None):
					ldata.next = None
				else:
					ldata.next = ldata.next.next
				break
			else:
				ldata = ldata.next
				Lenght += 1
		
	return llist


llist = Lnlist()
llist.head = Node(1)
llist.head.next=Node(2)
llist.head.next.next = Node(3)
fourth = Node(4)
llist.head.next.next.next = fourth
fifth = Node(5)
fourth.next = fifth

llist = push(0,llist)

llist = append(7,llist)

llist = insert(6,llist,5)

llist = insert(-1,llist,0)

llist = pop(llist,0)
llist = pop(llist,4)
llist = pop(llist,6)


llist = llist.head
while (llist != None):
	print(llist.data,end=" ")
	llist = llist.next


print()
		
