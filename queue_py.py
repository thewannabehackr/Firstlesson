class Queue:
	def __init__(self, head=None):
		self.storage= [head]

	def enqueue(self, element):
		self.storage.append(element)		


	def peek(self):
		return self.storage[0]
	
	def dequeue(self):
		top = self.storage[0]
		if len(self.storage) == 1:
			self.storage.clear()
		else:
			self.storage = self.storage[1:]	
		return top

q = Queue(1)
q.enqueue(2)
q.enqueue(3)

print(q.peek()) #1
print(q.dequeue()) #1

q.enqueue(4)
print(q.dequeue()) #2
print(q.dequeue()) #3
print(q.dequeue()) #4

q.enqueue(5)
print(q.peek()) #5


