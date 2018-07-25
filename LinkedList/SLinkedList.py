class ListNode:
	def __init__(self,x):
		self.val=x
		self.next=None

class SLinked_List:
	def __init__(self):
		self.head=None
		self.size=0
	def append(self,item):
		temp=ListNode(item)
		if self.head == None:
			self.head=temp
		else:
			current=self.head
			while current.next != None:
				current=current.next
			current.next=temp
		self.size+=1

	def __str__(self):
		s= '['
		i=0
		current=self.head
		while current != None:
			if i>0:
				s = s + ','
			dataObject = current.val
			if dataObject != None:
				s = s + "%s" % dataObject
				i = i + 1
			current = current.next
		s = s + ']'
		return s   