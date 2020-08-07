from generator import generating_pass

print("Welcome to PassGen!")
number = int(input("Please write your password lenght: "))

print("What'll be included in password (y/n)?")
details = []
details.append(input("Lowercase characters: ").lower())
details.append(input("Uppercase characters: ").lower())
details.append(input("Numbers: ").lower())
details.append(input("Symbols: ").lower())

print(generating_pass(number, details))
