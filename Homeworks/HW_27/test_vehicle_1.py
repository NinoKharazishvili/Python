import pytest
from vehicle_1 import Vehicle, ElectricVehicle

@pytest.fixture
def vehicle():
    return Vehicle("Range Rover", "SPORT SVR", 2020)

@pytest.fixture
def electric_vehicle():
    return ElectricVehicle("Tesla", "Model S", 2023)

def test_vehicle_initialization(vehicle):
    assert vehicle.brand == "Range Rover"
    assert vehicle.model == "SPORT SVR"
    assert vehicle.year == 2020
    assert vehicle.fuel_level == 0

def test_electric_vehicle_initialization(electric_vehicle):
    assert electric_vehicle.brand == "Tesla"
    assert electric_vehicle.model == "Model S"
    assert electric_vehicle.year == 2023
    assert electric_vehicle.charge_level == 0

def test_fuel_up(vehicle, electric_vehicle):
    assert vehicle.fuel_up == "Gas tank is now full or can move."
    assert electric_vehicle.fuel_up == "This vehicle has no fuel tank!"

def test_drive(vehicle, electric_vehicle):
    assert vehicle.drive == "The SPORT SVR is now driving."
    assert electric_vehicle.drive == "The Model S is now driving."

def test_charge(electric_vehicle):
    assert electric_vehicle.charge == "The vehicle is now charged."

if __name__ == "__main__":
    pytest.main()
