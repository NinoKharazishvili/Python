#3. მომხმარებელის შეაქვს მეტრების რაოდენობა. დაბეჭდეთ შესაბამისი მნიშვნელობა სანტიმეტრებში, დეციმეტრებში, მილიმეტრებში, მილში

meter = eval(input("Enter in meters: "))

centimeter = meter * 100
decimeter = meter * 10
millimeter = meter * 1000
mile = meter / 1609.344

print (meter, "meters is", centimeter, "centimeters")
print (meter, "meters is", decimeter, "decimeters")
print (meter, "meters is", millimeter, "millimeters")
print (meter, "meters is", mile, "miles")
