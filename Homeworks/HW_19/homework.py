class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value):
        self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self._year = value
        else:
            raise ValueError("Year must be an integer.")


# -------------------------------------- #
car = Car("Toyota", "Camry", 2022)

print("Brand:", car.brand)
print("Model:", car.model)
print("Year:", car.year)
