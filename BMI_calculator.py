
class Patient:

    def __init__(self, data=None):
        self.count_of_people = 0
        self.patient_data = data

    def criterias(self, bmi):
        if bmi <= 18.4:
            health_risks = "Malnutrition risk"
            category = "Underweight"
        elif 18.5 <= bmi <= 24.9:
            health_risks = "Low risk"
            category = "Normal weight"
        elif 25 <= bmi <= 29.9:
            health_risks = "Enhanced risk"
            category = "Overweight"
            self.count_of_people += 1
        elif 30 <= bmi <= 34.9:
            health_risks = "Medium risk"
            category = "Moderately obese"
        elif 35 <= bmi <= 39.9:
            health_risks = "High risk"
            category = "Severely obese"
        else:
            category = "Very severely obese"
            health_risks = "Very high risk"
        return category, health_risks

    def calculate_bmi(self):
        try:
            for data in self.patient_data:

                # getting height and weight from given data#
                height = data.get("HeightCm")
                weight = data.get("WeightKg")

                # calculating BMI #
                bmi = weight / (height / 100) ** 2

                # getting category, health_risks from  BMI #
                category, health_risks = self.criterias(bmi)

                # adding 3 new columns(bmi, category, health_risks) to existing data #
                data["bmi"] = bmi
                data["category"] = category
                data["health_risks"] = health_risks
        except Exception as e:
            raise Exception(e)

        return self.count_of_people


if __name__ == "__main__":
    data = [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96},
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
        ]
    obj = Patient(data=data)
    obj.calculate_bmi()
