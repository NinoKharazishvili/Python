# Single Responsibility Principle
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def set_details(self, title, author):
        self.title = title
        self.author = author
    
    def get_discount_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return discounted_price

# Open/Closed Principle
class Payment:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing Credit Card payment of ${amount}")

# Liskov Substitution Principle
class Vehicle:
    def fuel_capacity(self):
        return "100 liters"

class ElectricVehicle(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"

# Interface Segregation Principle
class AudioPlayer:
    def play_audio(self):
        print("Playing audio")

class VideoPlayer:
    def play_video(self):
        print("Playing video")

class MediaPlayer(AudioPlayer, VideoPlayer):
    pass

# Dependency Inversion Principle (DIP)
class Display:
    def show(self, data):
        print(data)

class ConsoleDisplay(Display):
    def show(self, data):
        print(f"Console: {data}")

class LCDdisplay(Display):
    def show(self, data):
        print(f"LCD Screen: {data}")

class WeatherStation:
    def report(self, display):
        weather_data = "Temperature: 25°C, Humidity: 60%"
        display.show(weather_data)

# ---------------------------------------------#
book = Book("Title", "Author")
book.set_details("New Title", "New Author")

payment = PayPalPayment()
payment.process_payment(100)

electric_car = ElectricVehicle()
print(electric_car.fuel_capacity())

media_player = MediaPlayer()
media_player.play_audio()
media_player.play_video()

weather_station = WeatherStation()
console_display = ConsoleDisplay()
lcd_display = LCDdisplay()

weather_station.report(console_display)
weather_station.report(lcd_display)
