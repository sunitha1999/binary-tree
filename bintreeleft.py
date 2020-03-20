#to print the nodes of a binary tree from root to bottom as visible fro left side of tree

a=[]
n=int(input("enter the height of binary tree: "))
h=(2**n)-1
for i in range(h):
	node=int(input("enter the element of binary tree: "))
	a.append(node)
print a


k=0
for item in a:
	i=a.index(item)
	if(i+1==(2**k) and item!=-1):
		print item
		k=k+1	
		
