import unittest
import run

class TestRun(unittest.TestCase):

    # Test that the test module is working!
    def test_is_this_thing_on(self):
        self.assertEqual(1, run.check())

    def test_string_to_boolean_true(self):
        self.assertEqual(True, run.string_to_boolean("True"))

    def test_string_to_boolean_false(self):
        self.assertEqual(False, run.string_to_boolean("False"))

    def test_string_to_boolean_invalid(self):
        self.assertRaises(ValueError, run.string_to_boolean, "x")
    
    def test_roundup_nearest_ten(self):
        self.assertEqual(30, run.roundup_nearest_ten(23.75))

    def test_roundup_nearest_one(self):
        self.assertEqual(24, run.roundup_nearest_one(23.75))

    def test_compute_temperature_settings_celsius(self):
        self.assertEqual({"celsius": "220","celsius_fan": "200","fahrenheit": "430","gas_mark": "7","user_temperature_type": 0}, run.compute_temperature_settings(220, "celsius"))

    def test_compute_temperature_settings_celsius_fan(self):
        self.assertEqual({"celsius": "200","celsius_fan": "180","fahrenheit": "400","gas_mark": "5","user_temperature_type": 1}, run.compute_temperature_settings(180, "celsius_fan"))

    def test_compute_temperature_settings_fahrenheit(self):
        self.assertEqual({"celsius": "250","celsius_fan": "230","fahrenheit": "475","gas_mark": "9","user_temperature_type": 2}, run.compute_temperature_settings(475, "fahrenheit"))

    def test_compute_temperature_settings_gas_mark(self):
        self.assertEqual({"celsius": "170","celsius_fan": "150","fahrenheit": "340","gas_mark": "3","user_temperature_type": 3}, run.compute_temperature_settings(3, "gas_mark"))

if __name__ == '__main__':
    unittest.main()
