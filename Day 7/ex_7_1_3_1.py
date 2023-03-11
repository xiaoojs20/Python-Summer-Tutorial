class Person:
    def __init__(self, name, age, weight, height, salary):
        self._name = name
        self.__age = age
        self.__weight = weight
        self.height = height
        self._salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be a string!')
        self._name = value

    @property
    def salary(self):
        sum_salary = 0
        for idx in range(len(self._salary)):
            sum_salary += self._salary[idx]

        return sum_salary/len(self._salary),sum_salary

    @salary.setter
    def salary(self, value):
        for idx in range(len(value)):
            if (not isinstance(value[idx], int)) and (not isinstance(value[idx], float)):
                raise ValueError("salary must be an int/float")
        else:
            self._salary = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if (not isinstance(value, int)) and (not isinstance(value, float)):
            raise ValueError("salary must be an int/float")
        else:
            self.__weight = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("salary must be an int/float")
        else:
            self.__age = value

    @property
    def BMI(self):
        return self.__weight / (self.height ** 2)


p1 = Person("Xiao", 18, 64, 1.75, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print([p1.name, p1.age, p1.weight, p1.height, p1.height, p1.BMI, p1.salary])
