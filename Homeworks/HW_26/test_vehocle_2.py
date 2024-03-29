from vehicle import Vehicle, ElectricVehicle
import unittest

class TestVehicle(unittest.TestCase):
  def setUp(self):
    print("setUp")

    self.v1 = Vehicle("Mazda", "Verisa", 2005)
    self.v2 = Vehicle("Toyota", "Aqua", 2017)
    self.v3 = Vehicle("Audi", "Q7", 2014)

    self.e1 = ElectricVehicle("Tesla", "Model S", 2022)
    self.e2 = ElectricVehicle("Tesla", "Model 5", 2019)
    self.e3 = ElectricVehicle("Tesla", "Model 3", 2018)
  

  def tearDown(self):
    print("tearDown\n")


  def test_fuel_up(self):
    print("test_fuel_up")

    self.assertEqual(self.v1.fuel_up, "Gas tank is now full or can move.")
    self.assertEqual(self.v2.fuel_up, "Gas tank is now full or can move.")

    self.v3.gaz_tank_size = 0
    self.assertEqual(self.v3.fuel_up, "Gas tank is empty and can not move.")

    self.assertEqual(self.e1.fuel_up, "This vehicle has no fuel tank!")
    self.assertEqual(self.e2.fuel_up, "This vehicle has no fuel tank!")
    self.assertEqual(self.e3.fuel_up, "This vehicle has no fuel tank!")
  

  def test_drive(self):
    print("test_drive")

    self.assertEqual(self.v1.drive, "The Verisa is now driving.")
    self.assertEqual(self.v2.drive, "The Aqua is now driving.")
    self.assertEqual(self.v3.drive, "The Q7 is now driving.")
    
    self.assertEqual(self.e1.drive, "The Model S is now driving.")
    self.assertEqual(self.e2.drive, "The Model 5 is now driving.")
    self.assertEqual(self.e3.drive, "The Model 3 is now driving.")
  

  def test_charge(self):
    print("test_charge")

    self.assertEqual(self.e1.charge, "The vehicle is now charged.")
    self.assertEqual(self.e2.charge, "The vehicle is now charged.")
    self.assertEqual(self.e3.charge, "The vehicle is now charged.")


# ===============
if __name__ == '__main__':
  unittest.main()