def super_sum(*args):
	''''
	Function that that takes in any number of numbers (or list of numbers) and sums them up.
	'''



	if args != ():
		#create an empty list
		my_list = []
		#Loop through the arguments first to get lists / integers
		for item in args:
			#check type of item
			if type(item) == list:
				#save them in a list variable
				my_list = my_list + item

			if type(item) == int:
				my_list.append(item)

		#use sum() function to add the numbers

		try:

			result = sum(my_list)

		except TypeError:
			return "Type not supported"

		return result



	else:
		return "empty"

