from BMI_calculator import *
import unittest

data = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]

invalid_data = [
    {"Gender": "Male", "WeightKg": 96},
    {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
    {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
    {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]


class TestBMICalculator(unittest.TestCase):

    def test_BMI_calculator_success(self):
        """test_BMI_calculator_success"""
        result = Patient(data=data).calculate_bmi()
        self.assertEqual(1, result)

    def test_BMI_calculator_failure(self):
        """test_BMI_calculator_failure"""
        with self.assertRaises(Exception):
            Patient(data=invalid_data).calculate_bmi()


if __name__ == '__main__':
    unittest.TestCase()
