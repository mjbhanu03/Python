class Vehicles:
  def __init__(self):
    self.__vehicle
    self.__tyres
    self.__power

  def start_engine(self, vehicle):
    self.__vehicle = f"{vehicle} engine started."
  
  def tyres(self, number):
    self.__tyres = number
  
  def hoursepower(self, power):
    self.__power = power


class Car(Vehicles):
    def __init__(self, carName, tyres, power):
      self.start_engine(carName)
      self.tyres(tyres)
      self.hoursepower(power)
      print(f"Your {carName} having {tyres} tyres and {power} Horse Power.")

class Bike(Vehicles):
    def __init__(self, bikeName, tyres, power):
      self.start_engine(bikeName)
      self.tyres(tyres)
      self.hoursepower(power)
      print(f"Your {bikeName} having {tyres} tyres and {power} Horse Power.")


car1 =Car("Ferrari", 4, 2500)
car2 = Car("BMW", 4, 1300)

bike1 = Bike("Ninja H2R", 2, 1500)
bike2 = Bike("R15", 2, 500)
