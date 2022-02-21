# 1] Create a class called
# Country

# which has a single class
# attribute called AVG_POPULATION.

#  Set it to some default
# value.

# The constructor takes the
# parameters country_name and country_code.

# The constructor must check
# that country_name and country_code are strings. If not it must throw a ValueError.

# The constructor must check
# if the country code is exactly 3 letters long. If not it must throw a ValueError.


# Write a method called
# country_short_form() which takes the country_name as a parameter and returns the first 2 letters of the country name in uppercase. Suitable validations must be done for the
# method.


# Write a class method called
# is_densly_populated(), which takes a single parameter `population` and returns true if the population is greater than AVG_POPULATION otherwise false. Suitable validations must be
# done for the method.


# Write a static method called
# world_avg_population(), which takes an array of numbers of the different country populations and returns the average of the numbers. Suitable validations must be done for the
# method.


# Write a method called
# formatted_country_name which returns a string containing the `country_name ( country_code)` [ ex - India ( IND) ]. Make this method into a property using decorators, and write a
# getter, setter, and a deleter for manipulating the values of country_name and country_code. Suitable validations must be done for the method.


class Country:

    AVG_POPULATION = 10000

    def __init__(self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code
    
    @property
    def country_name(self):
        return self._country_name

    @country_name.setter
    def country_name(self, d):
        if type(d) != str: raise  ValueError("Not a valid country name")
        self._country_name = d

    @property
    def country_code(self):
        return self._country_code

    @country_code.setter
    def country_code(self, v):
        if type(v)!=str or len(v)!=3: raise ValueError("Not a valid county code")
        self._country_code = v

    def country_short_form(self, country_name):
        return country_name[:2]
    
    @classmethod
    def is_densly_populated(self, population):
        if population > Country.AVG_POPULATION:
            return True
        else:
            return False

    @staticmethod
    def world_avg_population(arr):
        return sum(arr) / len(arr)

    def formatted_country_nam(self):
        return f"{self.country_name} ({self.country_code})"

country = Country("India", "IND")
print(country.country_short_form("India"))
print(Country.is_densly_populated(5000))
print(Country.world_avg_population([1,2,3,4,5]))
print(country.formatted_country_nam())

