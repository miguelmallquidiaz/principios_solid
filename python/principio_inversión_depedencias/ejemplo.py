"""
Crea un sistema de notificaciones.
Requisitos:
1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
2. El sistema de notificaciones no puede depender de las implementaciones específicas.
Instrucciones:
1. Crea la interfaz o clase abstracta.
2. Desarrolla las implementaciones específicas.
3. Crea el sistema de notificaciones usando el DIP.
4. Desarrolla un código que compruebe que se cumple el principio.
"""
from abc import ABC, abstractmethod

class Notifier(ABC):

    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando email con texto: {message}")


class PUSHNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando PUSH con texto: {message}")


class SMSNotifier(Notifier):
    def send(self, message: str):
        print(f"Enviando SMS con texto: {message}")


class NotificationService:

    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def notify(self, message: str):
        self.notifier.send(message)


# service = NotificationService(EmailNotifier())
# service = NotificationService(PUSHNotifier())
service = NotificationService(SMSNotifier())
service.notify("¡Hola, notificador!")