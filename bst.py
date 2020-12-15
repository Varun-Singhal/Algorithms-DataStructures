"""
BST insert, search, delete

Time - O(logn)(best), O(n) (average)
Soace - O(logn) (if done by recursion), O(1) (if done by loop iteration)
"""
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if self.value > value:
			if self.left is None:
				self.left = BST(value)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = BST(value)
			else:
				self.right.insert(value)
		return self

	def contains(self, value):
		if self.value == value:
			return True
		elif self.value > value:
			if self.left is None:
				return False
			else:
				return self.left.contains(value)
		else:
			if self.right is None:
				return False
			else:
				return self.right.contains(value)

	def remove(self, value, parent=None):
		if value < self.value and self.left is not None:
			#If smaller value, ignore the right sub tree
			self.left.remove(value, self)
		elif value > self.value and self.right is not None:
			#if larger value ignore the left sub tree
			self.right.remove(value,self)
		else:
			#If value matches
			if self.right is not None and self.left is not None:
				"""
				If 2 child exists, get min value from right sub tree
				place it to the to be deleted node , then delete 
				the value from right sub tree
				"""
				self.value = self.right.getMinValue()
				self.right.remove(self.value,self)
			elif parent is None:
				"""
				If only one child exists and the node is parent node
				"""
				if self.left is not None:
					#Delete the node and assign the next to root
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right is not None:
					#Delete the right node and assign the next to roott
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else:
					#Tree with single node, do nothing
					pass
			#When deleting the leaf node
			elif parent.left == self:
				parent.left = self.left if self.left is not None else self.right
			elif parent.right == self:
				parent.right = self.left if self.left is not None else self.right			
		return self
	
	def getMinValue(self):
		if self.left is None:
			return self.value
		else:
			return self.left.getMinValue()
