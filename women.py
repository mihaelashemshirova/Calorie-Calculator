from math import log
from calorie_calculator_program import CalorieCalculator


class Women(CalorieCalculator):

    def __init__(self, gender, age, weight, height, girth_above_navel, girth_through_navel, hips, neck, activity, deficit_surplus):
        super().__init__(gender, age, weight, height, girth_above_navel, girth_through_navel, hips, neck, activity, deficit_surplus)

    def body_fat_percent(self):
        tm_percent = 163.205 * log(self.girth_above_navel + self.hips - self.neck, 10) - 97.684 * log(self.height, 10) - 104.912
        return tm_percent

    def body_fat_kg(self):
        fat_kg = (self.weight / 100) * Women.body_fat_percent(self)
        return fat_kg

    def body_weight(self):
        activ_weight = self.weight - Women.body_fat_kg(self)
        return activ_weight

    def basal_metabolism(self):
        bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return bmr

    def daily_caloric_optimum(self):
        caloric_optimum = Women.basal_metabolism(self) * self.activity
        return caloric_optimum

    def caloric_intake_in_deficit(self):
        cal_optimum = Women.daily_caloric_optimum(self)
        cal_deficit = cal_optimum + (cal_optimum * self.deficit_surplus / 100)
        return cal_deficit
