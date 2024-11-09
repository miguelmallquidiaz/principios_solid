from abc import ABC, abstractmethod

"""
Crea un gestor de impresoras.
Requisitos:
1. Algunas impresoras sólo imprimen en blanco y negro.
2. Otras sólo a color.
3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
Instrucciones:
1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
2. Aplica el ISP a la implementación.
3. Desarrolla un código que compruebe que se cumple el principio.
"""

# Interfaces para cada una de las operaciones y cada impresera es capa de hacer

class PrinterInterface(ABC):
    @abstractmethod
    def print(self, document: str):
        pass

class ColorPrinterInterface(ABC):
    @abstractmethod
    def print_color(self, document:str):
        pass

class ScannerInterface(ABC):
    @abstractmethod
    def scan(self, document: str) -> str:
        pass

class FaxInterface(ABC):
    @abstractmethod
    def send_fax(self, document: str):
        pass

class Printer(PrinterInterface):
    def print(self, document:str):
        print(f"Imprimiendo en blanco y negro {document}")

class ColorPrinter(ColorPrinterInterface):
    def print_color(self, document:str):
        print(f"Imprimiendo a color {document}")

class Multifuncion(PrinterInterface, ColorPrinterInterface, ScannerInterface, FaxInterface):
    def print(self, document:str):
        print(f"Imprimiendo en blanco y negro {document}")
        
    def print_color(self, document:str):
        print(f"Imprimiendo a color {document}")
    
    def scan(self, document:str):
        print(f"Scaneando el documento {document}")

    def send_fax(self, document:str):
        print(f"Enviando por fax el documento {document}")