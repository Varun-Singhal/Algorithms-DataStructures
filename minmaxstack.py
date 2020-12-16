# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def peek(self):
		if len(self.stack)>0:
			return self.stack[-1]
		return

	def pop(self):
		if len(self.stack)>0:
			self.MinMax.pop()
			return self.stack.pop()
		return

	def push(self, number):
		self.stack.append(number)
		min_no = max_no = None
		if len(self.MinMax) == 0:
			min_no = number
			max_no = number
		else:
			if self.MinMax[-1]['min'] > number:
				min_no = number
			else:
				min_no = self.MinMax[-1]['min']

			if self.MinMax[-1]['max'] < number:
				max_no = number
			else:
				max_no = self.MinMax[-1]['max']

		self.MinMax.append({'min':min_no,'max':max_no})
		#print(self.stack, self.MinMax)

	def getMin(self):
		if len(self.MinMax)>0:
			return self.MinMax[-1]['min']
		return

	def getMax(self):
		if len(self.MinMax)>0:
			return self.MinMax[-1]["max"]
		return
	
	def __init__(self):
		self.MinMax = []
		self.stack = []