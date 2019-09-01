# Practice: Convert Student Object to a String
# Use the __str__ and __repr__ magic methods on your class to specify what an object's string representation should be. It's just like the toString() method in JavaScript.

# If you print a Student object. The output would look something like below.

# mike = Student()
# mike.first_name = "Mike"
# mike.last_name = "Ellis"
# mike.age = 35
# mike.cohort_number = 39

# print(mike)
# <__main__.Student object at 0x107133f60>
# But if you specify exactly what string should be returned from __str__ or __repr__, that will print out instead. If you implement the following method on your class...

# class Student:

#     def __str__(self):
#         return f"{self.full_name}"
# then the output will change

# print(mike)
# Mike Ellis
# Change your class so that any objects created from it will be represented as strings in the following format:

# Mike Ellis is 35 years old and is in cohort 39


class Student:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort = 0

    # first name getter and setter
    @property  # The getter
    def first_name(self):
        try:
            return self.__first_name  # Note there are 2 underscores here
        except AttributeError:
            return "no first name"

    @first_name.setter  # The setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for first name')

    # last name getter and setter
    @property  # The getter
    def last_name(self):
        try:
            return self.__last_name  # Note there are 2 underscores here
        except AttributeError:
            return "no last name"

    @last_name.setter  # The setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for last name')

    # age getter and setter
    @property  # The getter
    def age(self):
        try:
            return self.__age  # Note there are 2 underscores here
        except AttributeError:
            return "no age"

    @age.setter  # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer value for age')

    # cohort getter and setter
    @property  # The getter
    def cohort(self):
        try:
            return self.__cohort  # Note there are 2 underscores here
        except AttributeError:
            return "no cohort number assigned"

    @cohort.setter  # The setter
    def cohort(self, new_cohort):
        if type(new_cohort) is int:
            self.__cohort = new_cohort
        else:
            raise TypeError('Please provide a integer value for cohort')

    # fullname getter
    @property  # The getter
    def fullname(self):
        try:
            # Note there are 2 underscores here
            return self.__first_name + " " + self.__last_name
        except AttributeError:
            return "enter a valid value for both first name and last name"

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old and is in Cohort {self.cohort}.'


Mike = Student()
Mike.first_name = "Mike"
Mike.last_name = "Ellis"
Mike.age = 39
Mike.cohort = 33
print(Mike)
