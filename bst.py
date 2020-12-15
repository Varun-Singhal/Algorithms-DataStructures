class BST:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self,value):
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

	def contains(self, value):
		if self.value == value:
			return True
		elif self.value > value and self.left is not None:
			return self.left.contains(value)
		elif self.right is not None:
			return self.right.contains(value)
		else:
			return False


	def remove(self, value):
		pass


if __name__ == '__main__':
	root = BST(10)
	root.insert(20)
	root.insert(-2)
	root.insert(-5)
	root.insert(100)
	print(root.contains(100))
	print(root.contains(-5))

