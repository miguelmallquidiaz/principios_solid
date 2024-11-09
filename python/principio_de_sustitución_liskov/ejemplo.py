"""
Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
cumplir el LSP.
Instrucciones:
1. Crea la clase Vehículo.
2. Añade tres subclases de Vehículo.
3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
4. Desarrolla un código que compruebe que se cumple el LSP.
"""

# Cada vehículo puede ser trabajado de manera independiente e intercambiable 
# sin roperar la lógica. 
class Vehicle:
    def __init__(self, speed = 0):
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad {self.speed} Km/h")
    
    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad {self.speed} Km/h")

class Car(Vehicle):
    def accelerate(self, increment):
        return super().accelerate(increment)
    def brake(self, decrement):
        return super().brake(decrement)

class Motorcycle(Vehicle):
    def accelerate(self, increment):
        return super().accelerate(increment)
    
    def brake(self, decrement):
        return super().brake(decrement)

def test_vehicle(vehicle):
    vehicle.accelerate(2)
    vehicle.brake(2)

car = Car()
motorcycle = Motorcycle()

test_vehicle(motorcycle)
test_vehicle(car)