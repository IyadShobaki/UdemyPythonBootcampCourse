from math import e
def e_with_precision(n):
	return '%.*f'%(n,e)
if __name__=='__main__':
	correct_input = False
	while not correct_input:
		print('Percision must be between 1 and 51')
		percision = int(input('Number of decimal places: '))
		if 51 >= percision > 0:
			correct_input = True


	print(e_with_precision(percision))