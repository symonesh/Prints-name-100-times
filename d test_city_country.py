import unittest
from city_functions import city_function1
class test(unittest.TestCase):
    def test_first_and_last(self):
        formatted_names=city_function1('LV','USA','12331')
        self.assertEqual(formatted_names,'LV,USA,12331')
    unittest.main()
   