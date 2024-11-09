"""
Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
manejar diferentes aspectos como el registro de libros, la gestión de usuarios
y el procesamiento de préstamos de libros.
Requisitos:
1. Registrar libros: El sistema debe permitir agregar nuevos libros con
información básica como título, autor y número de copias disponibles.
2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
información básica como nombre, número de identificación y correo electrónico.
3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
tomar prestados y devolver libros.
Instrucciones:
1. Refactoriza el código: Separa las responsabilidades en diferentes clases
siguiendo el Principio de Responsabilidad Única.
"""

## La idea es separar cada clases que solo se encargue de una cosa en especifico

class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"Book: {self.title}, Author: {self.author}, Copies: {self.copies}"


class User:
    def __init__(self, name, id_number, email):
        self.name = name
        self.id_number = id_number
        self.email = email

    def __str__(self):
        return f"User: {self.name}, ID: {self.id_number}, Email: {self.email}"

class BookRegistry:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

class UserRegistry:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def find_user(self, id_number):
        for user in self.users:
            if user.id_number == id_number:
                return user
        return None

class LoanProcessor:
    def __init__(self, book_registry, user_registry):
        self.book_registry = book_registry
        self.user_registry = user_registry
        self.loans = {}

    def borrow_book(self, id_number, title):
        user = self.user_registry.find_user(id_number)
        book = self.book_registry.find_book(title)

        if user and book and book.copies > 0:
            book.copies -= 1
            if id_number in self.loans:
                self.loans[id_number].append(book)
            else:
                self.loans[id_number] = [book]
            return f"Book '{book.title}' borrowed by user {user.name}."
        return f"Book '{title}' is not available or user with ID {id_number} does not exist."

    def return_book(self, id_number, title):
        if id_number in self.loans:
            for book in self.loans[id_number]:
                if book.title == title:
                    book.copies += 1
                    self.loans[id_number].remove(book)
                    return f"Book '{title}' returned by user with ID {id_number}."
        return f"Book '{title}' was not borrowed by user with ID {id_number}."