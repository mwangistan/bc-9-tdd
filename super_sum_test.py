import unittest
from super_sum import super_sum

class SuperSumTest(unittest.TestCase):

	'''
	Super sum tests
	'''

	def test_value_error(self):
		#test if non supported types i.e dictionary, string
		self.assertEqual(super_sum(10, 5, [6, 's']), "Type not supported")

	def test_sum_of_integers(self):
		#sum of numbers
		self.assertEqual(super_sum(10, 5, 6, 9), 30)

	def test_empty(self):
		#Test if empty
		self.assertEqual(super_sum(), 'empty')

	def test_result_type(self):
		#Test if return values are integers
		self.assertIs(type(super_sum(10)), int)

	def test_nested_list_result(self):
		#Test result when arguments have nested lists
		self.assertEqual(super_sum([5, 6], [4, 5], 10), 30)
		self.assertEqual(super_sum([10, 5], 5), 20)





if __name__ == '__main__':
	unittest.main()
