from Hashtable import Hashtable
import random

# The objective of this program is to determine the efficiency of the simple hash function
# by inserting a random string of random length into a hashtable of a given size and determining
# the number of collisions in each spot


SIZE = 1000
MAX_WORD_LENGTH = 10
AMMOUNT_WORDS = 10000

tbl = Hashtable(SIZE)
for i in range(1,AMMOUNT_WORDS):
	string = ""
	for i in range(0, random.randint(1, MAX_WORD_LENGTH)):
		string+= chr(random.randint(65, 90)) #ascii A-Z
	print("%i for word: %s"%(tbl.hashWord(string),string))