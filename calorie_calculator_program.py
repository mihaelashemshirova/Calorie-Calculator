from math import log
from abc import ABC, abstractmethod


class CalorieCalculator(ABC):
    def __init__(self, gender: str, age: int, weight: float, height: int, girth_above_navel: int, girth_through_navel: int, hips: int, neck: int, activity: float, deficit_surplus: int):
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
        self.girth_above_navel = girth_above_navel
        self.girth_through_navel = girth_through_navel
        self.hips = hips
        self.neck = neck
        self.activity = activity
        self.deficit_surplus = deficit_surplus

    @abstractmethod
    def body_fat_percent(self):
        ...

    @abstractmethod
    def body_fat_kg(self):
        ...

    @abstractmethod
    def body_weight(self):
        ...

    @abstractmethod
    def basal_metabolism(self):
        ...

    @abstractmethod
    def daily_caloric_optimum(self):
        ...

    @abstractmethod
    def caloric_intake_in_deficit(self):
        ...

    def daily_fluid_intake(self):
        if self.age <= 30:
            min_liquids = 0.035 * self.weight
            max_liquids = 0.040 * self.weight
            return f"{min_liquids:.1f} - {max_liquids:.1f}"
        elif self.age <= 54:
            min_liquids = 0.03 * self.weight
            max_liquids = 0.035 * self.weight
            return f"{min_liquids:.1f} - {max_liquids:.1f}"
        elif self.age <= 65:
            liquids = 0.03 * self.weight
            return f"{liquids:.1f}"
        else:
            liquids = 0.25 * self.weight
            return f"{liquids:.1f}"


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


class Men(CalorieCalculator):

    def __init__(self, gender, age, weight, height, girth_above_navel, girth_through_navel, hips, neck, activity, deficit_surplus):
        super().__init__(gender, age, weight, height, girth_above_navel, girth_through_navel, hips, neck, activity, deficit_surplus)

    def body_fat_percent(self):
        tm_percent = 86.010 * log(self.girth_above_navel - self.neck, 10) - 70.041 * log(self.height, 10) + 30.30
        return tm_percent

    def body_fat_kg(self):
        fat_kg = (self.weight / 100) * Men.body_fat_percent(self)
        return fat_kg

    def body_weight(self):
        activ_weight = self.weight - Men.body_fat_kg(self)
        return activ_weight

    def basal_metabolism(self):
        bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        return bmr

    def daily_caloric_optimum(self):
        caloric_optimum = Men.basal_metabolism(self) * self.activity
        return caloric_optimum

    def caloric_intake_in_deficit(self):
        cal_optimum = Men.daily_caloric_optimum(self)
        cal_deficit = cal_optimum + (cal_optimum * self.deficit_surplus / 100)
        return cal_deficit
