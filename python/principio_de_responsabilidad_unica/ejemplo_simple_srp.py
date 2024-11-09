"""
Ejercicio:    
"""

# Incorrecto
# necesita una funcionalidad que guarde en base de datos y otra para enviar el email

class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

    def save_to_database(self):
        pass

    def send_email(self):
        pass

# Correcto
"""
La clase acabara reducido a solo representar al usuario y si escala cada servicio es independiente.
""" 

class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email

class UserService:
    def save_to_database(self, user):
        pass

class EmailService:
    def send_email(self, email, message):
        pass
