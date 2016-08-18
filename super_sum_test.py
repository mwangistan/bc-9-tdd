import unittest
from super_sum import super_sum

class SuperSumTest(unittest.TestCase):

	'''
	Super sum tests
	'''

	#test if non supported types i.e dictionary, string

	def test_value_error(self):
		self.assertEqual(super_sum(10, 5, [6, 's']), "Type not supported")

	#sum of numbers
	def test_sum_of_integers(self):
		self.assertEqual(super_sum(10, 5, 6, 9), 30)
		


	#Test if empty

	def test_empty(self):
		self.assertEqual(super_sum(), 'empty')

	#Test if return values are integers

	def test_result_type(self):
		self.assertIs(type(super_sum(10)), int)

	#Test result when arguments have nested lists

	def test_nested_list_result(self):
		self.assertEqual(super_sum([5, 6], [4, 5], 10), 30)
		self.assertEqual(super_sum([10, 5], 5), 20)





if __name__ == '__main__':
	unittest.main()
