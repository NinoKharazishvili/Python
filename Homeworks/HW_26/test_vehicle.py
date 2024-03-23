import unittest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle(unittest.TestCase):
    def test_vehicle_creation(self):
        car = Vehicle("Range Rover", "SPORT SVR", 2020)
        self.assertEqual(car.brand, "Range Rover")
        self.assertEqual(car.model, "SPORT SVR")
        self.assertEqual(car.year, 2020)
        self.assertEqual(car.gaz_tank_size, 45)
        self.assertEqual(car.fuel_level, 0)

    def test_fuel_up(self):
        car = Vehicle("Range Rover", "SPORT SVR", 2020)
        car.fuel_up
        self.assertEqual(car.fuel_level, 45)

    def test_drive(self):
        car = Vehicle("Toyota", "SPORT SVR", 2020)
        self.assertEqual(car.drive, "The SPORT SVR is now driving.")

class TestElectricVehicle(unittest.TestCase):
    def test_electric_vehicle_creation(self):
        ev = ElectricVehicle("Tesla", "Model S", 2021)
        self.assertEqual(ev.brand, "Tesla")
        self.assertEqual(ev.model, "Model S")
        self.assertEqual(ev.year, 2021)
        self.assertEqual(ev.battery_size, 85)
        self.assertEqual(ev.charge_level, 0)

    def test_charge(self):
        ev = ElectricVehicle("Tesla", "Model S", 2021)
        ev.charge
        self.assertEqual(ev.charge_level, 100)

    def test_fuel_up(self):
        ev = ElectricVehicle("Tesla", "Model S", 2021)
        self.assertEqual(ev.fuel_up, "This vehicle has no fuel tank!")

if __name__ == '__main__':
    unittest.main()
