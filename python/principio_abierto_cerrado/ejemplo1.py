"""
Ejercicio

Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
Requisitos:
- Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
Instrucciones:
1. Implementa las operaciones de suma, resta, multiplicación y división.
2. Comprueba que el sistema funciona.
3. Agrega una quinta operación para calcular potencias.
4. Comprueba que se cumple el OCP.

"""
from abc import ABC, abstractmethod

# Se hereda de ABC es una clase abstracta que actua como una interfaz
class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

# En esta parte hereda los metodos pero yo le puedo dar la operación que necesita
class Addition(Operation):
    def execute(self, a, b):
        return a + b
class Substration(Operation):
    def execute(self, a, b):
        return a - b
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
class Division(Operation):
    def execute(self, a, b):
        return a / b
    
class Calculator:
    def __init__(self) -> None:
        self.operations = {}
    
    def add_operation(self, name, operation):
        self.operations[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operations:
            raise ValueError(f"La operación {name} no esta soportada.")
        return self.operations[name].execute(a, b)

calculator = Calculator()
calculator.add_operation("addition", Addition())
calculator.add_operation("subtration", Substration())
calculator.add_operation("multiplication", Multiplication())
calculator.add_operation("division", Division())

print(calculator.calculate("division", 0, 12))