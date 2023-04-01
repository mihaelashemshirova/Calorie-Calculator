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
