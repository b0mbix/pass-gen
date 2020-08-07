from generator import generating_pass

print("Welcome to PassGen!")
try:
    #pass lenght
    number = int(input("Please write your password lenght: "))

    #what has to be in pass
    print("What'll be included in password (y/n)?")
    details = []
    details.append(input("Lowercase characters: ").lower())
    details.append(input("Uppercase characters: ").lower())
    details.append(input("Numbers: ").lower())
    details.append(input("Symbols: ").lower())

    #details have to be y/n
    for i in details:
        if i != 'y' and i != 'n':
            raise ValueError

    #generating only if all values are valid
    print(generating_pass(number, details))

#if any value is invalid
except ValueError:
    print("Invalid input!")
