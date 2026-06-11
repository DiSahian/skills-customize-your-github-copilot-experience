from helpers import greet_user, calculate_rectangle_area, is_palindrome

# Task 1

def main():
    name = input("Enter your name: ")
    print(greet_user(name))

    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    area = calculate_rectangle_area(length, width)
    print(f"Rectangle area: {area}")

    text = input("Enter a word or phrase: ")
    result = is_palindrome(text)
    print(f"Is palindrome: {result}")

if __name__ == "__main__":
    main()
