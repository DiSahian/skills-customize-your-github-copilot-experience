import string


def greet_user(name):
    return f"Hello, {name}!"


def calculate_rectangle_area(length, width):
    return length * width


def is_palindrome(text):
    normalized = ''.join(ch.lower() for ch in text if ch.isalnum())
    return normalized == normalized[::-1]
