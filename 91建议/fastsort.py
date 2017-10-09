"""
快速排序算法，每一次都将小的数分在一起，大的数分在一起
"""

def quicksort(array):
	less = []
	greater = []
	if len(array) <= 1:
		return array
	pivot = array.pop()
	for x in array:
		if x <= pivot: 
			less.append(x)
			print "less add " + str(x)
		else:
			greater.append(x)
			print "greater add " + str(x)
	return quicksort(less) + [pivot] + quicksort(greater)

array = [3,5,23,4,32,345,5,6,6,7,234,5,6,7,8]
a = quicksort(array)
print a