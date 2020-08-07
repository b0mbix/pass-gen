from generator import generating_pass

print("Welcome to PassGen!")
try:
    number = int(input("Please write your password lenght: "))

    print("What'll be included in password (y/n)?")
    details = []
    details.append(input("Lowercase characters: ").lower())
    details.append(input("Uppercase characters: ").lower())
    details.append(input("Numbers: ").lower())
    details.append(input("Symbols: ").lower())

    for i in details:
        if i != 'y' and i != 'n':
            raise ValueError

    print(generating_pass(number, details))
except ValueError:
    print("Invalid input!")
