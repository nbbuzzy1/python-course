import unittest
import add_five


class TestMain2(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = add_five.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'asdfa'
        result = add_five.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = add_five.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = add_five.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')


if __name__ == '__main__':
    unittest.main()
