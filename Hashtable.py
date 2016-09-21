
class Hashtable:

	#Based on the has function, the bigger the table, the less collisions that will occur
	def __init__(self, size):
		self.size = size-1
		self.table = [0]*self.size

	# converts the string into an index to store
	def hashWord(self, str1):
		total = 0
		for char in str1:
			total = total + ord	(char)
		total = total%self.size
		self.table[total] += 1
		return self.table[total]
		# returns the number of times that this spot was accessed