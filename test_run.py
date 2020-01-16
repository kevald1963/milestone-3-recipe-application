import unittest
import run

class TestRun(unittest.TestCase):

    # Test that the test module is working!
    def test_is_this_thing_on(self):
        self.assertEqual(1, run.check())

    def string_to_boolean_true(self):
        self.assertEqual(True, run.string_to_boolean())

if __name__ == '__main__':
    unittest.main()
